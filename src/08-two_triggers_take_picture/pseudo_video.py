import datetime, time
import os

from gpiozero import MotionSensor
from picamera import PiCamera


def get_timestamp():
    date = datetime.datetime.now()
    return '%02d.%02d-%02d:%02d:%02d' % (date.month, date.day, date.hour, date.minute, date.second)

PROBING_INTERVAL = 0.1
PICTURE_INTERVAL = 0

cam = PiCamera(resolution=(800,600))
pir1 = MotionSensor(23)
pir2 = MotionSensor(24)
false_positives = [0,0]

print('Big brother is watching you')

current_alert = None
picture_counter = 0
slack = 0

while True:
    m1 = pir1.motion_detected
    m2 = pir2.motion_detected

    if m1 and not m2:
        false_positives[0] +=1
    elif m2 and not m1:
        false_positives[1] +=1
    total_number_of_false_positives = sum(false_positives)
    if total_number_of_false_positives%100==0 and total_number_of_false_positives!=0:
        print('%s false alerts' % (','.join(str(x) for x in false_positives)))

    all_sensors_agree_that_there_is_motion = m1 and m2
    at_least_one_sensor_sees_motion_and_there_is_an_alert = current_alert is not None and (m1 or m2)
    no_sensor_sees_motion_but_slack_is_active = (not m1 and not m2) and slack>0 
    photo_must_be_taken = all_sensors_agree_that_there_is_motion or at_least_one_sensor_sees_motion_and_there_is_an_alert or no_sensor_sees_motion_but_slack_is_active

    if photo_must_be_taken:
        if current_alert is None:
            date = datetime.datetime.now()
            timestamp = get_timestamp()
            print('[%s] ALERT' % timestamp)
            current_alert = '/home/pi/Desktop/photos/%s' % timestamp
            os.mkdir(current_alert)
            picture_counter = 0
        else:
            if no_sensor_sees_motion_but_slack_is_active:
                slack -= 1
            else:
                slack = 3
        cam.capture('%s/%03d.jpg' % (current_alert,picture_counter))
	print('*', picture_counter)
	picture_counter += 1
    else:
        if current_alert is not None:
            print('[%s] end (%d pictures)' % (get_timestamp(), picture_counter))
            current_alert = None

    time.sleep(PROBING_INTERVAL if current_alert is None else PICTURE_INTERVAL)
    
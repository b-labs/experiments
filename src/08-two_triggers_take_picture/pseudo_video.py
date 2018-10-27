import datetime, time
import os

from gpiozero import MotionSensor
from picamera import PiCamera


def get_timestamp():
    date = datetime.datetime.now()
    return '%02d.%02d-%02d:%02d:%02d' % (date.month, date.day, date.hour, date.minute, date.second)

PROBING_INTERVAL = 0.1
SLACK = 30

cam = PiCamera(resolution=(800,600))
pir1 = MotionSensor(23)
pir2 = MotionSensor(24)
false_positives = [0,0]

print('Big brother is watching you')

alert = False
last_alert_directory = None
last_picture_time = None
picture_counter = 0

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

    now = datetime.datetime.now()
    time_since_last_picture = (now-last_picture_time).total_seconds() if last_picture_time else None
	
    all_sensors_agree_that_there_is_motion = m1 and m2
    at_least_one_sensor_sees_motion_and_there_is_an_alert = alert and (m1 or m2)
    alert = all_sensors_agree_that_there_is_motion or at_least_one_sensor_sees_motion_and_there_is_an_alert

    if alert:
        is_new_event = time_since_last_picture>SLACK if last_picture_time else True
        if is_new_event:
            timestamp = get_timestamp()
            print('[%s] ALERT' % timestamp)
            last_alert_directory = '/home/pi/Desktop/photos/%s' % timestamp
            os.mkdir(last_alert_directory)
            picture_counter = 0
        cam.capture('%s/%03d-%d%d.jpg' % (last_alert_directory,picture_counter,+m1,+m2))
        print('*', picture_counter)
        picture_counter += 1
        last_picture_time = now if picture_counter<999 else None
    else:
        time.sleep(PROBING_INTERVAL)

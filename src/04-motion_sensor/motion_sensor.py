from gpiozero import MotionSensor
from signal import pause
import datetime


print("Connecting ...")
pir = MotionSensor(24)
print("Connected")

def sleep() :
    message("Zzzzz...")

def alert() :
    message("ALERT")

def message(text) :
    date = datetime.datetime.now()
    print '%02d:%02d:%02d' % (date.hour,date.minute,date.second) + " " + text


pir.when_motion = alert
pir.when_no_motion = sleep


pause()
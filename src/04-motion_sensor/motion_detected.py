from gpiozero import MotionSensor
import time


print("Connecting ...")
pir = MotionSensor(14)
print("Connected")

while True:
    if pir.motion_detected:
        print("ALERT")
    else:
        print (".")
    time.sleep(1)
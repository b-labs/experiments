from gpiozero import MotionSensor, LED
from picamera import PiCamera
from signal import pause
from time import sleep

cam = PiCamera()
pir = MotionSensor(21)
led1 = LED(4)
led2 = LED(17)
n = 0

def name():
    return 'photo-%03d.jpg'%n

def rafale():
    global n
    led2.on()
    i = 0
    while i<10:
      led1.on()
      cam.capture('/home/pi/Desktop/photos/%s'%name())
      print('picture taken')
      n=n+1
      i=i+1

      sleep(0.5)
      led1.off()
      sleep(0.5)
    led2.off()
    


pir.when_motion = rafale
pause()
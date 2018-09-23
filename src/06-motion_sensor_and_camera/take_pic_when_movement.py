from gpiozero import MotionSensor
from picamera import PiCamera
from signal import pause

cam = PiCamera()
pir = MotionSensor(21)
n = 0

def name():
    return 'photo-%03d.jpg'%n

def picture():
    global n
    print('taking picture...')
    cam.capture('/home/pi/Desktop/photos/%s'%name())
    print('picture taken')
    n=n+1


pir.when_motion = picture
pause()
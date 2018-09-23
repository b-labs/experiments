import time
import picamera

cam = picamera.PiCamera()

cam.capture('/home/pi/Desktop/photos/photo.jpg')
print('picture taken')
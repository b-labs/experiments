from gpiozero import LED
import time

led1 = LED(4)
led2 = LED(17)

led1.on()
time.sleep(3)
led1.off()

led2.on()
time.sleep(3)
led2.off()
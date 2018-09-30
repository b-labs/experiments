from gpiozero import LED
import time


led = LED(18)

DURATION = 0.2
N = 5
i = 0
 
while i < N :
  led.on()
  time.sleep(DURATION)
  led.off()
  time.sleep(DURATION)
  i = i + 1

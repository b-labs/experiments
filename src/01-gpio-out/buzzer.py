from gpiozero import LED
import time

buzzer = LED(14)

BUZZTIME = 0.05
RATIO_BETWEEN_BUZZ_AND_SLEEP = 20

for i in range(10):
    buzzer.on()
    time.sleep(BUZZTIME)
    buzzer.off()
    time.sleep(BUZZTIME*RATIO_BETWEEN_BUZZ_AND_SLEEP)
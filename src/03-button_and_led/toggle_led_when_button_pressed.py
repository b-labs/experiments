from gpiozero import Button, LED
from signal import pause

button = Button(23)
led = LED(18)

button.when_pressed = lambda: led.on()
button.when_released = lambda: led.off()
pause()
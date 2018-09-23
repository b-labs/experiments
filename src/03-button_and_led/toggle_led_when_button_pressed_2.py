from gpiozero import Button, LED
from signal import pause


button = Button(23)
led = LED(18)

def toggle():
    led.toggle()

button.when_pressed = toggle
pause()
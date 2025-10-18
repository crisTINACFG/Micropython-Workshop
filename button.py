# Diagnostic: print raw button value frequently
from machine import Pin
from time import sleep

BUTTON_PIN = 16
# Try PULL_DOWN first (button should connect to 3.3V when pressed)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

print("Raw monitor: button pressed should show 1 when you press the button.")
while True:
    print(button.value())
    sleep(0.2)

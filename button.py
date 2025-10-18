# Diagnostic: print raw button value frequently
import machine
from machine import Pin
import utime

BUTTON_PIN = 16
# Change PULL_DOWN <-> PULL_UP to match how your button is wired.
# If button connects to 3.3V when pressed -> use Pin.PULL_DOWN
# If button connects to GND when pressed  -> use Pin.PULL_UP
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

# give pin a moment to settle, then read idle level
utime.sleep_ms(50)
idle = button.value()
print("Detected idle value:", idle)
print("Will print once per press (debounced).")

while True:
    val = button.value()
    if val != idle:
        # debounce
        utime.sleep_ms(20)
        if button.value() != idle:
            print("Button pressed")
            # wait for release
            while button.value() != idle:
                utime.sleep_ms(20)
    utime.sleep_ms(50)

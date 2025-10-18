from machine import Pin, PWM
from time import sleep

# === Define pin for RED ===
RED_PIN = 13

# === Constants ===
BRIGHTNESS = 0.5           # 0.0–1.0 (50%)
MAX_COLOUR_VALUE = 255
COMMON_ANODE = True         # Your LED is common anode

# === Setup PWM ===
red = PWM(Pin(RED_PIN))
red.freq(1000)

def show_red(value):
    """Set brightness of red LED (0–255)"""
    # Scale 0–255 to 0–65535
    r_val = int(value * 65535 / MAX_COLOUR_VALUE * BRIGHTNESS)
    
    if COMMON_ANODE:
        # invert: low = on
        r_val = 65535 - r_val
    
    red.duty_u16(r_val)

# === Test sequence ===
while True:
    print("Red full brightness")
    show_red(255)
    sleep(1)

    print("Half brightness")
    show_red(128)
    sleep(1)

    print("Dim")
    show_red(50)
    sleep(1)

    print("Off")
    show_red(0)
    sleep(1)

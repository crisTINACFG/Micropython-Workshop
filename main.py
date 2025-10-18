from machine import Pin
from utime import sleep

# === DEFINE PINS ===
RED_PIN = 18    # Change to your Red GPIO
GREEN_PIN = 19  # Change to your Green GPIO
BLUE_PIN = 20   # Change to your Blue GPIO

# === DEFINE LED TYPE ===
COMMON_CATHODE = True  # True if common cathode, False if common anode

# === SETUP PINS ===
red = Pin(RED_PIN, Pin.OUT)
green = Pin(GREEN_PIN, Pin.OUT)
blue = Pin(BLUE_PIN, Pin.OUT)

# === COLOR CONTROL FUNCTION ===
def set_color(r, g, b):
    """Turn on/off each color (1=on, 0=off)"""
    if COMMON_CATHODE:
        red.value(r)
        green.value(g)
        blue.value(b)
    else:  # Common anode
        red.value(not r)
        green.value(not g)
        blue.value(not b)

# === SIMPLE LOOP TO TEST COLORS ===
while True:
    set_color(1, 0, 0)  # Red
    print("Red")
    sleep(1)
    set_color(0, 1, 0)  # Green
    print("Green")
    sleep(1)
    set_color(0, 0, 1)  # Blue
    print("Blue")
    sleep(1)
    set_color(1, 1, 1)  # White
    print("White")
    sleep(1)

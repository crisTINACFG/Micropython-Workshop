import machine
import utime
from machine import Pin, PWM
from time import sleep

RED_PIN = 16
BRIGHTNESS = 1   
MAX_COLOUR_VALUE = 255

red = PWM(Pin(RED_PIN))
red.freq(1000)
ACTIVE_LOW = False

def show_red(value):
    r_val = int(value * 65535 / MAX_COLOUR_VALUE * BRIGHTNESS)
    if ACTIVE_LOW:
        r_val = 65535 - r_val
    red.duty_u16(r_val)
BUZZER_PIN = 15
pwm = machine.PWM(machine.Pin(BUZZER_PIN))
DEFAULT_DUTY = 32768

# Note frequencies (Hz)
# DEFINE NEW NOTES HERE IF NEEDED
C4 = 261
D4 = 294
E4 = 329
F4 = 349
G4 = 392
A4 = 440
B4 = 494
# C5 = 523
# E5 = 659
# G5 = 784
# D5 = 587
# C6 = 1047
# F5 = 698
# A5 = 880

def play_tone(freq, ms):
    if freq == 0:
        pwm.duty_u16(0)
        utime.sleep_ms(ms)
        return
    pwm.freq(int(freq))
    #HINT: Turn on LED when playing a note here, choose any brightness you like
    pwm.duty_u16(DEFAULT_DUTY)
    utime.sleep_ms(ms)
    pwm.duty_u16(0)
    #HINT: Turn off LED after the note here
    utime.sleep_ms(30)

def play_song():
    #"Twinkle Twinkle Little Star" (short)
    #(c4, 400) means play C4 for 400 ms
    melody = [
        (C4, 400), (C4, 400), (G4, 400), (G4, 400),
        (A4, 400), (A4, 400), (G4, 800),
        (F4, 400), (F4, 400), (E4, 400), (E4, 400),
        (D4, 400), (D4, 400), (C4, 800),
    ]

    for note, dur in melody:
        play_tone(note, dur)
        

try:
    play_song()
finally:
    pwm.duty_u16(0)
    pwm.deinit()

# Your task:
# 1. Modify the melody to play a different song instead!
    # you can use any song you like, just make sure to define the notes
    # Define the new notes where the others are defined, if you need a pause, use (0, duration_in_ms).

    # you can ask ChatGPT to help you with the melody if you need. 
    # e.g. "Can you help me write a short melody for 'Happy Birthday'? Give me the notes and durations (in ms) and order they should be played in."
    # you can even ask it to give you the song in the format used in the code above by providing it an example.

# 2. Turn the LED on and off for each note.
    # Make it so that when a note is played, the LED lights up (you can choose the brightness you like from 0-255).   
    # Read through the code where there are comments like "HINT"
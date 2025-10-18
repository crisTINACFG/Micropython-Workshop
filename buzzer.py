# import machine
# import utime

# buzzer = machine.Pin(15, machine.Pin.OUT)

# buzzer.value(1)
# utime.sleep(0.1)
# buzzer.value(0)


import machine
import utime

# PWM buzzer on Pin 15
BUZZER_PIN = 15
pwm = machine.PWM(machine.Pin(BUZZER_PIN))
DEFAULT_DUTY = 32768  # ~50% duty (0-65535)

# Note frequencies (Hz)
C4 = 261
D4 = 294
E4 = 329
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

def play_tone(freq, ms):
    if freq == 0:
        pwm.duty_u16(0)
        utime.sleep_ms(ms)
        return
    pwm.freq(int(freq))
    pwm.duty_u16(DEFAULT_DUTY)
    utime.sleep_ms(ms)
    pwm.duty_u16(0)
    # short gap between notes
    utime.sleep_ms(30)

def play_song():
    # "Twinkle Twinkle Little Star" (short)
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
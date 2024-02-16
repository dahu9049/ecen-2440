from machine import Pin
import time

counter = 0
debounce = 0
btn = Pin(5, Pin.IN, Pin.PULL_UP)
while True:
    if not btn.value() and ((time.ticks_ms() - debounce) > 200):
        print("Button Pressed")
        counter += 1
        debounce = time.ticks_ms()
        print(f'Counter = ', counter)
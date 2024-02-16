from machine import Pin
import time

interrupt_flag = 0
count = 0
debounce_time = 0

btn = Pin(5, Pin.IN, Pin.PULL_UP)
led = Pin("LED", Pin.OUT)

def callback(pin):
    global interrupt_flag, debounce_time
    if(time.ticks_ms() - debounce_time) > 500:
        interrupt_flag = 1
        debounce_time = time.ticks_ms()
btn.irq(trigger=Pin.IRQ_FALLING, handler=callback)

while True:
    if interrupt_flag:
        interrupt_flag = 0
        print("Interrupt Occured, Button Pressed")
        led.toggle()




import ir_rx
from machine import Pin
import time
import uasyncio as asyncio
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging
# Callback function to execute when an IR code is received

led_pins = {
    0x01: Pin(18, Pin.OUT), # Command 0x01 associated with LED on Pin 18
    0x02: Pin(19, Pin.OUT), # Command 0x02 associated with LED on Pin 19
    0x03: Pin(20, Pin.OUT), # Command 0x03 associated with LED on Pin 20
    0x04: Pin(21, Pin.OUT), # Command 0x04 associated with LED on Pin 21
}

def turn_off_led(led_pin):
    time.sleep(0.5) # Non-blocking wait for 2 secondas
    led_pin.value(0) # Turn off LED

def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
    if data in led_pins: # If the command is one of the known commands
        led_pin = led_pins[data] # Get the corresponding LED Pin object
        led_pin.value(1) # Turn on the LED
        # asyncio.create_task(turn_off_led(led_pin))
        turn_off_led(led_pin)


# Setup the IR receiver
ir_pin = Pin(16, Pin.IN, Pin.PULL_UP) 
# Adjust the pin number based on your wiring
ir_receiver = NEC_8(ir_pin, callback=ir_callback)
# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)
# Main loop to keep the script running
while True:
 pass # Execution is interrupt-driven, so just keep the script alive
# main.py
# MicroPython script for ESP8266 (using uPyCraft)
# Controls an LED based on an LDR sensor reading.

from machine import Pin, ADC
import time

# --- Configuration ---
# LDR Sensor connected to the only ADC pin (A0 on most boards).
# The ADC reads values from 0 (Darkest) to 1024 (Brightest) on the ESP8266.
LDR_PIN = 0
adc = ADC(LDR_PIN)

# LED connected to a digital pin (D4/GPIO2 is common on NodeMCU).
# If you are using the built-in LED, setting Pin(2, Pin.OUT) is correct.
# Note: The built-in LED on many ESP8266 boards is ACTIVE-LOW (0=ON, 1=OFF).
LED_PIN = 2 
led = Pin(LED_PIN, Pin.OUT)

# Threshold: Adjust this value based on your LDR/resistor setup and environment.
# Values below this threshold will be considered "dark" (LED ON).
LIGHT_THRESHOLD = 500 

print("LDR Sensor and LED control starting...")

def set_led_state(is_dark):
    """Sets the LED state based on whether it is dark or bright."""
    
    # We use active-low logic for the built-in LED (0=ON, 1=OFF)
    if is_dark:
        led.value(0) # Turn LED ON
        print("-> DARK: LED ON")
    else:
        led.value(1) # Turn LED OFF
        print("-> BRIGHT: LED OFF")

try:
    while True:
        # Read the analog value from the LDR (0-1024)
        ldr_value = adc.read()
        
        print(f"LDR Reading: {ldr_value}")
        
        # Check if the reading is below the set threshold
        if ldr_value < LIGHT_THRESHOLD:
            set_led_state(True)
        else:
            set_led_state(False)
            
        # Wait for a short period before reading again
        time.sleep(1)

except KeyboardInterrupt:
    # Gracefully handle stop command in the REPL
    led.value(1) # Turn LED OFF on exit
    print("\nScript stopped by user.")
    
# Clean up is not strictly necessary in MicroPython's simple loop, 
# but good for habit.
finally:
    pass

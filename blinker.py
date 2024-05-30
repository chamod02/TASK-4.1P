import gpiod
import time

# Define LED Pin
LED_PIN = 17

# Define location of GPIO
chip = gpiod.Chip('gpiochip4')

# Create a variable
led_line = chip.get_line(LED_PIN)

# Set the LED as an output
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

try:
    # Infinite loop to blink the LED
    while True:
        led_line.set_value(1)  # Turn on LED
        time.sleep(0.25)            # Delay for 0.25 seconds
        led_line.set_value(0)   # Turn off LED
        time.sleep(0.25)            # Delay for 0.25 seconds
    # Clean up the GPIO settings before exiting
finally:
    led_line.set_value(0)
    led_line.release()

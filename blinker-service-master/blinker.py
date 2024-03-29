import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

while True: # Run forever
    GPIO.output(8, GPIO.HIGH) # Turn on
    GPIO.output(10, GPIO.LOW)
    sleep(1)                  # Sleep for 1 second
    
    GPIO.output(8, GPIO.LOW)  # Turn off
    GPIO.output(10, GPIO.HIGH)
    sleep(1)                  # Sleep for 1 second value to low (off)
# Import the rpi.gpio module. 
import RPi.GPIO as GPIO 
from time import sleep
# Set the mode of numbering the pins
GPIO.setmode(GPIO.BCM) 
# GPIO pin 8 is the output.
GPIO.setup(26, GPIO.OUT)  

# Initialise GPIO 26 to high (true) so that the LED is off. 
GPIO.output(26,True) 
while True:

	GPIO.output(26,1)
        sleep(1)
        GPIO.output(26,0)
        sleep(1)

GPIO.cleanup()

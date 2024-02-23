import RPi.GPIO as GPIO
import time

# Set up GPIO pins for servos
servo1_pin = 17  # GPIO17 for servo 1 (LEFT)
servo2_pin = 18  # GPIO18 for servo 2 (RIGHT)

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)

# Create PWM instances for servos
servo1_pwm = GPIO.PWM(servo1_pin, 50)  # 50 Hz PWM frequency
servo2_pwm = GPIO.PWM(servo2_pin, 50)

# Start PWM
servo1_pwm.start(0)
servo2_pwm.start(0)

def rotate_servos():
    # Rotate servo 1 counterclockwise (adjust start position)
    servo1_pwm.ChangeDutyCycle(9)  # Adjust start position
    time.sleep(0.4)  # Adjust sleep time as needed for desired rotation
    servo1_pwm.ChangeDutyCycle(10)  # Adjust stop position
    time.sleep(0.4)  # Adjust sleep time as needed for desired rotation
    servo1_pwm.ChangeDutyCycle(0)  # Stop rotation

    # Rotate servo 2 clockwise (adjust start position)
    servo2_pwm.ChangeDutyCycle(2)  # Adjust start position
    time.sleep(0.4)  # Adjust sleep time as needed for desired rotation
    servo2_pwm.ChangeDutyCycle(3)  # Adjust stop position
    time.sleep(0.4)  # Adjust sleep time as needed for desired rotation
    servo2_pwm.ChangeDutyCycle(0)  # Stop rotation

    print("active")

def return_to_neutral():
    # Return servos to neutral position
    servo1_pwm.ChangeDutyCycle(7.5)  # Neutral position for servo 1
    servo2_pwm.ChangeDutyCycle(7.5)  # Neutral position for servo 2
    time.sleep(0.4)
    print("nuetral")

try:
    while True:
        user_input = input("Enter a string: ")
        if user_input.lower() == "smile":
            rotate_servos()
        else:
            return_to_neutral()                                             

except KeyboardInterrupt:
    servo1_pwm.stop()
    servo2_pwm.stop()
    GPIO.cleanup()

import RPi.GPIO as GPIO
import time

# Set up GPIO pins for servos
servo1_pin = 17  # GPIO17 for servo 1 (RIGHT)
servo2_pin = 18  # GPIO18 for servo 2 (LEFT)

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
    # Rotate servo 1 counterclockwise (quarter turn)
    servo1_pwm.ChangeDutyCycle(0)  # Change duty cycle for rotation (slightly reduced)
    time.sleep(0.4)  
    servo1_pwm.ChangeDutyCycle(3) 

    # Rotate servo 2 clockwise (quarter turn)
    servo2_pwm.ChangeDutyCycle(3)  # Change duty cycle for rotation (slightly reduced)
    time.sleep(0.4)  
    servo2_pwm.ChangeDutyCycle(0)  

def return_to_active():
    # Return servos to neutral position
    servo1_pwm.ChangeDutyCycle(7.5)  # Neutral position for servo 1
    servo2_pwm.ChangeDutyCycle(7.5)  # Neutral position for servo 2
    time.sleep(0.5)  

try:
    while True:
        user_input = input("Enter a string: ")
        if user_input.lower() == "smile":
            rotate_servos()
        else:
            return_to_active()
        

except KeyboardInterrupt:
    servo1_pwm.stop()
    servo2_pwm.stop()
    GPIO.cleanup()

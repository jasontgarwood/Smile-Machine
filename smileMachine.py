import RPi.GPIO as GPIO

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
    # Rotate servo 1 
    servo1_pwm.ChangeDutyCycle(7.5)  # Neutral position for servo 1

    # Rotate servo 2
    servo2_pwm.ChangeDutyCycle(0)  # Change duty cycle for rotation (slightly reduced)
    servo2_pwm.ChangeDutyCycle(3)  

 # Return servos to neutral position
def return_to_nuetral():
   
    # Rotate Servo 1
    servo1_pwm.ChangeDutyCycle(0)  # Change duty cycle for rotation (slightly reduced)  
    servo1_pwm.ChangeDutyCycle(3) 

    # Rotate servo 2
    servo2_pwm.ChangeDutyCycle(7.5)  # Neutral position for servo 2 

# keyboard input trigger (swap this for another input if you'd like!!)
try:
    while True:
        user_input = input("Enter a string: ")
        if user_input.lower() == "smile":
            rotate_servos()
        else:
            return_to_nuetral()  

# end function with crtl C
except KeyboardInterrupt:
    servo1_pwm.stop()
    servo2_pwm.stop()
    GPIO.cleanup()
from gpio import *

def turnon():
    GPIO.output(pin, GPIO.HIGH)
    
def turnoff():
    GPIO.output(pin, GPIO.LOW)

from gpio import *
import random
import time

def turnon():
    GPIO.output(pin, GPIO.HIGH)
    
def turnoff():
    GPIO.output(pin, GPIO.LOW)
    
def fast():
    time.sleep(.random.randint(10,500))
    

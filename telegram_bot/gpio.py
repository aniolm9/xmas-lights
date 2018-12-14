# Importo les llibreries
import RPi.GPIO as GPIO

# Faig la configuració bàsica del GPIO
pin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

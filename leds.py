import Adafruit_BBIO.GPIO as GPIO

leds = {
	"GREEN": "P9_12",
	"YELLOW": "P9_15",
	"RED": "P9_42"
}

def init_leds():
	for color in leds:
		GPIO.setup(leds[color], GPIO.OUT)

def turn_on(color):
	GPIO.output(leds[color], GPIO.HIGH)

def turn_off(color):
	GPIO.output(leds[color], GPIO.LOW)
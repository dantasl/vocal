import Adafruit_BBIO.GPIO as GPIO

house = {
	"KITCHEN": "P9_12",
	"BATHROOM": "P9_15",
	"LIVINGROOM": "P9_42"
}

def init_leds():
	for room in house:
		GPIO.setup(house[room], GPIO.OUT)


def turn_on(room):
	GPIO.output(house[room], GPIO.HIGH)


def turn_off(room):
	GPIO.output(house[room], GPIO.LOW)


def turn_all_on():
    for room in house:
        turn_on(room)


def turn_all_off():
    for room in house:
        turn_off(room)
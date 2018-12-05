import Adafruit_BBIO.GPIO as GPIO


house = {
	"KITCHEN": "P9_12",
	"BATHROOM": "P9_15",
	"LIVINGROOM": "P9_42"
}


def decode_command(command):
	command = command.decode().lower()
	if command == "kitchen on":
		turn_on("KITCHEN")
	elif command == "kitchen off":
		turn_off("KITCHEN")
	elif command == "bathroom on":
		turn_on("BATHROOM")
	elif command == "bathroom off":
		turn_off("BATHROOM")
	elif command == "living room on":
		turn_on("LIVINGROOM")
	elif command == "living room off":
		turn_off("LIVINGROOM")
	elif command == "all on":
		turn_all_on()
	elif command == "all off":
		turn_all_off()
	else:
		print("Could not decode command.")
		return False
	return True	


def init_leds():
	for room in house:
		print("Component from {} configured, mode out.".format(room))
		GPIO.setup(house[room], GPIO.OUT)


def turn_on(room):
	print("Turning on {}".format(room))
	GPIO.output(house[room], GPIO.HIGH)


def turn_off(room):
	print("Turning off {}".format(room))
	GPIO.output(house[room], GPIO.LOW)


def turn_all_on():
    for room in house:
        turn_on(room)


def turn_all_off():
    for room in house:
        turn_off(room)
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) #specifies that we are referring to the pins by the number of the pin printed on the board

switch_in  = [12,16,18] 
switch_out = [7,13,15,29,31]


def switch_init(switch_in,switch_out):
     print("Output pins")
     for i in switch_out:
        GPIO.setup(i,GPIO.OUT) #used to set the pins to high or low
        print(i)
     print("Input pins")
     for j in switch_in:
         GPIO.setup(j,GPIO.IN) #used to read
         print(j)

#12,16,18 are used as input pins and they are used to read the HIGH/LOW .If any of them are pressed it goes HIGH.
         
def which_char(character):
    count = 0
    for i in switch_in:
        if GPIO.input(i):
            time.sleep(.3)
            return character[count]
        count = count+1
    return '#'


def switch_output():
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    c1 = which_char(['a','f','k'])

    GPIO.output(7,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    c2 = which_char(['b','l','g'])

    GPIO.output(7,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    c3 = which_char(['c','h','m'])

    GPIO.output(7,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(29,GPIO.HIGH)
    GPIO.output(31,GPIO.LOW)
    c4 = which_char(['d','i','n'])

    GPIO.output(7,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.HIGH)
    c5 = which_char(['e','j','o'])

    if c1 != '#':
        return c1

    if c2 != '#':
        return c2

    if c3 != '#':
        return c3

    if c4 != '#':
	return c4

    if c5 != '#':
        return c5


switch_init(switch_in,switch_out)





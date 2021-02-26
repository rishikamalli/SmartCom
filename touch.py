import sys
import time

import Adafruit_MPR121.MPR121 as MPR121


print('Adafruit MPR121 Capacitive Touch Sensor Test')

cap = MPR121.MPR121()


if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

print('Press Ctrl-C to quit.')
last_touched = cap.touched()


def touch_output():
    global last_touched
    current_touched = cap.touched()
    key = -1
    # Check each pin's last and current state to see if it was pressed or released.
    for i in range(12):
        pin_bit = 1 << i
        #if the sensor is touched and not touched before 
        if current_touched & pin_bit and not last_touched & pin_bit:
	    pass
            #print('{0} touched!'.format(i))
	#if the sensor is releasedb
        if not current_touched & pin_bit and last_touched & pin_bit:
            #print('{0} released!'.format(i))
            key = i
    last_touched = current_touched
    time.sleep(0.2)
    return key


def which_char_sensor():
    value = "pqrstuvwxyz*" # * is the send option
    key = touch_output()
    if key > -1:
	#print(value[key])
	return value[key]
    else:
	return -1
"""
while True:
      value = which_char_sensor()
      if value != -1:
          print value

"""

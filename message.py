import serial

import time

MOBILE_NUMBER = "7259984757"
#baud is the measure of speed of communication over a data channel. Unit for pulses per second
ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate

def send_message(m):
    print(m)
    print('AT'+'\r\n')  #AT is the attention command. Required by wireless and dial up modem to interact with a computer machine
    ser.write('AT'+'\r\n') #checks interaction between the computer and modem. Returs OK if correct else ERROR.
    time.sleep(.5)

    print('AT+CMGF=1'+'\r\n') #Set as SMS mode. Command name in text: MessageFormat
    ser.write('AT+CMGF=1'+'\r\n')
    time.sleep(.5)

    print('AT+CSCS='+'"GSM"'+'\r\n') #used to specify the character set to display the address_text. Command name in text: set TE Character Set
    ser.write('AT+CSCS'+'"GSM"'+'\r\n') #GSM default alphabets
    time.sleep(.5)

    print('AT+CMGS='+'"+91'+MOBILE_NUMBER+'\"'+'\r\n') #Send SMS to the Number provided. Command name in text: send Message as SMS 
    ser.write('AT+CMGS='+'"+91'+MOBILE_NUMBER+'\"'+'\r\n')
    time.sleep(.5)

    print("MESSAGE:"+m)
    ser.write(m+'\r\n') #carriage return
    time.sleep(.5)
    ser.write('\x1A')# CTRL-Z
    print("Completed...")


"""
while True:
    msg = "Glove-Pi"
    send_message(msg) 
    while True:
	pass
"""

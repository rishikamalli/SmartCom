
import send
import message
import touch
import switch

msg = ""

while True:
    c2 =  switch.switch_output()
    if c2 != '#' and c2 != None:
        print(c2)
	send.client_sock.send(c2)
        msg += c2

    c1 = touch.which_char_sensor()
    if(c1 != -1) and (c1 != '*'):
        print c1
	send.client_sock.send(c1)
        msg += c1

    if c1 == '*':
        print "The Message is",msg
	message.send_message(msg)
        msg = ""


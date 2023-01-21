from machine import Pin, UART
import time

uart = UART(0, 9600)
none_recieved = False

while True:
    message = ""
    while uart.any():
        command = uart.readline()
        if command:
            message += str(command.decode('utf-8'))
            none_recieved = True
        time.sleep(0.01)
    if none_recieved == True:
        message = "Message: " + message
        uart.write(message.encode())
        print(message)
        none_recieved = False
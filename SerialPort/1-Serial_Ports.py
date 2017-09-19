import serial
ser=serial.Serial('COM15', 9600)
print(ser.name)         # check which port was really used
print(ser)
ser.write(b'hello')     # write a string
ser.close()             # close port

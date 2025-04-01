import serial
import time

ser = serial.Serial('/dev/ttyACM0', 57600, timeout = 1)
ser.reset_input_buffer()

def SerialSetup():
    ser = serial.Serial('/dev/ttyACM0', 57600, timeout = 1)
    ser.reset_input_buffer()

def ReadSerialData():
    line = ser.readline().decode('utf-8').rstrip()
    print(line)

def WriteSerialStringData(incoming):
    ser.write(incoming+b"\n")

def WriteSerialIntData(incoming):
    encodedIncoming = str(incoming).encode('utf-8')
    ser.write(encodedIncoming+b"\n")

import serial
import time

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0', 115200, timeout=100)
	ser.reset_input_buffer()
	
	while True:
                val = 1600
                valEncode = str(val).encode('utf-8')
                ser.write(b"n\n")
                ser.write(b"2\n")
                ser.write(valEncode+b"\n")

                #ser.write(b"n\n"+b"2\n"+valEncode+b"\n")
                
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                time.sleep(.01)

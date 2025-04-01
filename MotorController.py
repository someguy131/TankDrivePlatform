import serial
import time

import SerialComms

class MotorCtrl:
    MCid = 999
    MCpwm = 0

    #old code without serial class
    #ser = serial.Serial('/dev/ttyACM0', 57600, timeout = 1)
    #ser.reset_input_buffer()
    
    #initialize the motor controller class
    def __init__(self, MCidIn, MCpwmIn):
        self.MCid = int(MCidIn)
        self.MCpwm = MCpwmIn
        
        print("Motor ",MCidIn," initialized!")
    
    #send a new pwm value to the motor controller
    def MC_updatePwm(self, idIN, pwmIN):
        #init Serial com with baud rate of 
        #print(idIN)
        #print(pwmIN)

        SerialComms.WriteSerialStringData(b"n")
        SerialComms.WriteSerialIntData(idIN)
        SerialComms.WriteSerialIntData(pwmIN)

        SerialComms.ReadSerialData()

        ''' old code without serial class
        encodedID = str(idIN).encode('utf-8')
        encodedPWM = str(pwmIN).encode('utf-8')
        
        #send updated information over serial to device
        
        self.ser.write(b"n\n")#notify that new data set is coming
        
        self.ser.write(encodedID+b"\n") #send ID to controller
        
        self.ser.write(encodedPWM+b"\n") #send PWM value to controller

        line = self.ser.readline().decode('utf-8').rstrip()
        print(line)
        '''
        

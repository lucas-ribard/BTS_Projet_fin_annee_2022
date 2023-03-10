# lsusb to check device name
#dmesg | grep "tty" to find port name
import serial
import time

if __name__ == '__main__':
    
    print('Running. Press CTRL-C to exit.')
    #se co au port serial AMA0
    with serial.Serial("/dev/ttyUSB0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    cmd=input("Enter command : ")
                    arduino.write(cmd.encode())
                    time.sleep(1) #wait for arduino to answer
                    while arduino.inWaiting()==0: pass
                    if  arduino.inWaiting()>0: 
                        answer=arduino.readline()
                        print(answer)
                        arduino.flushInput() #remove data after reading
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
                
                
                
                #print(answer[0:len(answer)-2])
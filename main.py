import serial,time
import os

cmd ="Z"
with serial.Serial("/dev/ttyACM0", 9600, timeout =1) as arduino:
    time.sleep(0.1)
    if arduino.isOpen():
        print("Arduino board connected!".format(arduino.port))
        print('Running...\nPress CTRL-C to exit.')
        try:
            while True:
                arduino.write(cmd.encode())
                time.sleep(0.1) # wait for arduino to answer
                while arduino.inWaiting() == 0: pass
                if arduino.inWaiting() > 0:
                    answer = arduino.readline()
                    if str(answer).startswith("b'Fr"): #Front camera
                        channel = 0
                        print("Front hit, start detection")
                        cmd = "R"
                        arduino.write(cmd.encode())
                        os.system(f"python3 /home/reef19/ParkingGuard/ParkingGuard.py {channel}")
                        time.sleep(15) 
                    
                    elif str(answer).startswith("b'Ba"): # Back camera
                        channel = 2
                        print("Back hit, start detection")
                        cmd = "R"
                        arduino.write(cmd.encode())
                        os.system(f"python3 /home/reef19/ParkingGuard/ParkingGuard.py {channel}")
                        time.sleep(15)                         
                    
                    else:
                        cmd ="Z"
                        #print(answer)
                    
                    arduino.flushInput() #remove data after reading
        except KeyboardInterrupt:
            print("KeyboardInterrupt has been caught.")
            

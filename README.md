# ParkingGuard
Parking Guard is a Real-Time vehicle protection system. 

How It works:
1. Vibration sensors are sampled at a high frequency by the Arduino. 
2. Once an impact is detected, information about the impact's location (forward/backward) is transmitted to the Raspberry Pi via UART communication.
3. Relevant camera and neural network start operating to identify pre-defined objects (vehicles/humans).
4. An email is sent to the user containing information (time and date, impact location) and images of the offending object.


System structor:

![image](https://github.com/rif281/ParkingGuard/assets/102466625/0a382787-0fa6-4833-b8d2-2b0324ffdc76)


The system:

<img src="https://github.com/rif281/ParkingGuard/assets/102466625/a8f79cc2-760d-4420-9561-a0faf54d8d2d" alt="Alt Text" width="600" height="300" />



The project contains 3 code snippets:
1. Arduino code (coded in C)
2. Main - running on RBP. coded in Python.
3. ParkingGuard - running on RBP. coded in Python.



Arduino flowchart:

<img src="https://github.com/rif281/ParkingGuard/assets/102466625/b8cf8406-ba86-4f4d-afa9-05a589ff99cd" alt="Alt Text" height="600" />




Main flowchart:

<img src="https://github.com/rif281/ParkingGuard/assets/102466625/6b9cff83-a4a9-4f9b-9592-7450469b954c" alt="Alt Text" height="600" />




ParkingGuard flowchart:


<img src="https://github.com/rif281/ParkingGuard/assets/102466625/e3e09e36-e020-4ac0-8389-967cc1d315ef" alt="Alt Text" height="600" />





.

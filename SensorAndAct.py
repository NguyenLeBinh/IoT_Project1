print("Sensors and Actuators")

import time
import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    #return commPort
    return "/dev/ttyUSB0"
portName = "/dev/ttyUSB0"

#portName = "/dev/ttyUSB1"
print(portName)



try:
    ser = serial.Serial(port=portName, baudrate=9600)
    print("Open successfully")
    print(ser)
except:
    print("Can not open the port")

#relay1_ON  = [0, 6, 0, 0, 0, 255, 200, 91]
#relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]


relay1_ON  = [2, 6, 0, 0, 0, 255, 200, 91]
relay1_OFF = [2, 6, 0, 0, 0, 0, 136, 27]
relay2_ON  = [3, 6, 0, 0, 0, 255, 200, 91]
relay2_OFF = [3, 6, 0, 0, 0, 0, 136, 27]
relay3_ON  = [4, 6, 0, 0, 0, 255, 200, 91]
relay3_OFF = [4, 6, 0, 0, 0, 0, 136, 27]

def setDevice1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)
    time.sleep(1)
    print(serial_read_data(ser))
def setDevice2(state):
    if state == True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)
    time.sleep(1)
    print(serial_read_data(ser))
def setDevice3(state):
    if state == True:
        ser.write(relay3_ON)
    else:
        ser.write(relay3_OFF)
    time.sleep(1)
    print(serial_read_data(ser))
    
def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0
while True:
    
    setDevice1(True)
    print("ON1")
    setDevice2(True)
    print("ON2")
    setDevice3(True)
    print("ON3")
    time.sleep(2)
    setDevice1(False)
    print("OFF1")
    setDevice2(False)
    print("OFF2")
    setDevice3(False)
    print("OFF3")
    time.sleep(2)




soil_temperature =[1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    serial_read_data(ser)
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)

while True:
    print("TEST SENSOR")
    print(readMoisture())
    time.sleep(1)
    print(readTemperature())
    time.sleep(1)

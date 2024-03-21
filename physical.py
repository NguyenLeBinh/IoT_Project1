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
if "USB Serial" in strPort:
  splitPort = strPort.split(" ")
commPort = (splitPort[0])
return commPort

portName = getPort() 
print(portName)
if portName != "None":
  ser = serial.Serial(port=portName, baudrate=9600)

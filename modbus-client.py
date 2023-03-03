#!/usr/bin/env python3
from pyModbusTCP.client import ModbusClient
from time import sleep
from random import randint
import sys

hostClient = 'localhost'
portClient = 502 
initReg = 0
numofReg = 5

try:
    client = ModbusClient(host=hostClient, port=portClient)
except ValueError:
    print("Error with host or port params")

if client.open():
    print("Modbus client opened!")
else:
    sys.exit("Error opening Modbus client connection")

while True:
    client.write_single_register(initReg, randint(0,65534))
    sleep(0.7)
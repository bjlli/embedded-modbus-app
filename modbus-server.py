#!/usr/bin/env python3
from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

hostServer = "localhost"
portServer = 502

# Create an instance of ModbusServer
server = ModbusServer(hostServer, portServer, no_block=True)

print("Start server...")
server.start()
print("Server is online - CTRL C to exit")

while True:
    continue

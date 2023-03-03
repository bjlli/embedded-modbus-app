#!/usr/bin/env python3
from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep


hostServer = 'localhost'
portServer = 502
regAddr = 0

# Create an instance of ModbusServer

bank = DataBank()
server = ModbusServer(host=hostServer, port=portServer, no_block=True, data_bank=bank)

print("Start server...")
server.start()
print("Server is online - CTRL C to exit")

while True:
    srv_info = server.ServerInfo
    print("The value of register 0 is: " + str(bank.get_holding_registers(regAddr, 1, None)))
    sleep(0.5)

    

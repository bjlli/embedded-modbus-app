from pyModbusTCP.client import ModbusClient

hostClient = 'localhost'
portClient = 502 
unitID = 1
initReg = 400
numofReg = 7
regs_wr_list = [12,24,32,70,80,90,4]

try:
    client = ModbusClient(hostClient, portClient, unitID)
except ValueError:
    print("Error with host or port params")

if client.open():
    print("Opened")
    client.write_multiple_registers(initReg,regs_wr_list)
    regs_rd_list = client.read_holding_registers(initReg, numofReg)
    print(regs_rd_list)
else:
    print("Error opening client connection")

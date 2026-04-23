import subprocess
import numpy as np
import time
import can
import os
import cantools
import re
        

fields = ("runtime", 'rpm', 'clt', 'map', 'mat', 'tps', 'adv_deg', 'afttgt1', 'AFR1', 'batt')

db = cantools.database.load_file("MS3.dbc")

print(f"#!/bin/bash")

print("echo Starting test...")

print("while true; do")

##################################################################################


msg_obj = db.get_message_by_name("megasquirt_gp0")
for n in range(0, 12500, 500):
    data = msg_obj.encode({
    "rpm": n,
    "pw2": 0,
    "pw1": 0,
    "seconds": n/100
    })

    message = can.Message(arbitration_id=msg_obj.frame_id, data=data)

    data_hex = ''.join(f'{b:02X}' for b in data)
    id_hex = f'{message.arbitration_id:03X}'

    command  = "cansend can0 " + id_hex + "#" + data_hex

    print("sleep 0.01")
    print(command)

for n in range(12500, -500, -500):
    data = msg_obj.encode({
    "rpm": n,
    "pw2": 0,
    "pw1": 0,
    "seconds": n/100
    })

    message = can.Message(arbitration_id=msg_obj.frame_id, data=data)

    data_hex = ''.join(f'{b:02X}' for b in data)
    id_hex = f'{message.arbitration_id:03X}'

    command  = "cansend can0 " + id_hex + "#" + data_hex

    print("sleep 0.01")
    print(command)


msg_obj = db.get_message_by_name("megasquirt_gp2")
for n in range(0, 250, 25):
    data = msg_obj.encode({
    "clt": n,
    "mat": 0,
    "map": 0,
    "baro": 0
    })

    message = can.Message(arbitration_id=msg_obj.frame_id, data=data)

    data_hex = ''.join(f'{b:02X}' for b in data)
    id_hex = f'{message.arbitration_id:03X}'

    command  = "cansend can0 " + id_hex + "#" + data_hex

    print("sleep 0.01")
    print(command)

for n in range(250, 0, -25):
    data = msg_obj.encode({
    "clt": n,
    "mat": n/10,
    "map": n/10,
    "baro": 0
    })

    message = can.Message(arbitration_id=msg_obj.frame_id, data=data)

    data_hex = ''.join(f'{b:02X}' for b in data)
    id_hex = f'{message.arbitration_id:03X}'

    command  = "cansend can0 " + id_hex + "#" + data_hex

    print("sleep 0.01")
    print(command)
    


##################################################################################


print("done")



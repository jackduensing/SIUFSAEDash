import subprocess
import numpy as np
import time
import can
import os
import cantools

fields = ("runtime", 'rpm', 'clt', 'map', 'mat', 'tps', 'adv_deg', 'afttgt1', 'AFR1', 'batt')

db = cantools.database.load_file("MS3.dbc")

msg_obj = db.get_message_by_name("megasquirt_gp0")

print(f"!#/bin/bash")

print("echo Starting test...")

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

    print("sleep 0.125")
    print(command)



msg_obj = db.get_message_by_name("megasquirt_gp3")

data = msg_obj.encode({
    "afr2_old": 0,
    "afr1_old": 0,
    "batt": 14.5,
    "tps": 0
})

message = can.Message(arbitration_id=msg_obj.frame_id, data=data)

data_hex = ''.join(f'{b:02X}' for b in data)
id_hex = f'{message.arbitration_id:03X}'

command  = "cansend can0 " + id_hex + "#" + data_hex

#print(command)



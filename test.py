import numpy as np
import time
import can
import os
import cantools

fields = ("runtime", 'rpm', 'clt', 'map', 'mat', 'tps', 'adv_deg', 'afttgt1', 'AFR1', 'batt')

db = cantools.database.load_file("MS3.dbc")

msg_obj = db.get_message_by_name("megasquirt_dash0")

data = msg_obj.encode({
    "rpm": 5000,
    "clt": 225,
    "map": 0,
    "tps": 0
})

message = can.Message(arbitration_id=msg_obj.frame_id, data=data)

data = str(data)

data = data[1:].replace("\\", "").replace("x", "",).replace("'", "")

id = str(hex(message.arbitration_id)).replace("x", "")

print(f"cansend can0 {id[1:]}#{data}")


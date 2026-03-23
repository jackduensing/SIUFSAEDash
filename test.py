import numpy as np
import time
import can
import os
import cantools

fields = ("runtime", 'rpm', 'clt', 'map', 'mat', 'tps', 'adv_deg', 'afttgt1', 'AFR1', 'batt')

db = cantools.database.load_file("MS3.dbc")

bus = can.Bus(channel="can0", interface="socketcan", bitrate=500000)

def send_msg(field, value):

    if field not in fields:
        print("invalid field")

    msg_obj = db.get_message_by_name("test_msg")

    data = msg_obj.encode({field:value})

    message = can.Message(arbitration_id=msg_obj.frame_id, data=data)

    bus.send(message)


send_msg('rpm', 5000)
time.sleep(5)
send_msg('clt', 225)

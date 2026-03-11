from multiprocessing import shared_memory
import numpy as np
import time
import can
import os
import cantools

def run(mem_name, type):

    fields = ("runtime", 'rpm', 'clt', 'map', 'mat', 'tps', 'adv_deg', 'afttgt1', 'AFR1', 'batt')

    print(f"From process can, recieved {mem_name}")

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=type, buffer=shared_container.buf)

    #data['RPM'] = 5000.00
    
    bus = can.Bus(channel="can0", interface="socketcan", bitrate=500000)
    db = cantools.database.load_file("MS3.dbc")

    first_flag = 0

    while True:
        try:

            message = bus.recv()
            if message == None:     #returns none or message, if no message, skip
                continue

            else:
                decoded_data = db.decode_message(message.arbitration_id, message.data)

                for key, value in decoded_data:
                    if key in fields:
                        #lock
                        value == data[key]
                        if first_flag == 0:
                            data["timestamp"] = 
                        #todo add timestamping/uptime/runtime
                        

        except cantools.database.DecodeError:
            continue

        except Exception as e:
            #log error
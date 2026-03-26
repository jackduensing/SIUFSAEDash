from multiprocessing import shared_memory
import numpy as np
import time
import can
import os
import cantools

def run(mem_name, car_type, lock):

    print("Starting CAN")

    fields = ("runtime", 'rpm', 'clt', 'map', 'mat', 'tps', 'adv_deg', 'afttgt1', 'AFR1', 'batt')

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=car_type, buffer=shared_container.buf)
    
    bus = can.Bus(channel="can0", interface="socketcan", bitrate=500000)
    db = cantools.database.load_file("MS3.dbc")

    while True:
        try:

            print("waiting for message...")
            message = bus.recv()
            if message == None:     #returns none or message, if no message, skip
                print(f"message returned none type")
                continue

            else:
                decoded_data = db.decode_message(message.arbitration_id, message.data)

                for key, value in decoded_data.items():
                    if key in fields:
                        with lock:   
                            print(f"{key}:{value}")                                            
                            data[key] = value
                            data["timestamp"] = time.monotonic() - data["start_time"]       #uses the start_time field to create a "time since start"
                        
        except cantools.database.DecodeError:       #frame is not in dbc file, continue
            continue

        except KeyboardInterrupt:
            break

        except Exception as e:
            with open("log.txt", "a") as file:
                print(f"{e}\n", file=file)
            break

    shared_container.close()
    bus.shutdown()
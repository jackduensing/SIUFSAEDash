import time
from multiprocessing import shared_memory
import numpy as np
import pandas as pd
import os
from datetime import datetime

def run(mem_name, car_type, lock, log_flag):

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=car_type, buffer=shared_container.buf)

    #todo: once I have the flashdrive, create a permanent mount point
    file_path = "/mnt/logUSB"

    while True:
        time.sleep(1)
        try:
            with lock:
                now = datetime.now()
                toSave = pd.DataFrame(data)
                toSave["time"] = now.strftime("%H:%M:%S")
        except Exception as e:
                with open("/mnt/logUSB/log.txt", "a") as file:
                    print(f"{e}\n", file=file) 
                break

        if os.path.exists(file_path):
            try:
                toSave.to_csv(file_path + "/log.csv", mode='a', index=False, header=False)
            except Exception as e:
                with open("/mnt/logUSB/log.txt", "a") as file:
                    print(f"{e}\n", file=file) 
                break
            except KeyboardInterrupt:
                break

    shared_container.close()
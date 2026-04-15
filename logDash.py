import time
from multiprocessing import shared_memory
import numpy as np
import pandas as pd
import os
from datetime import datetime

def run(mem_name, car_type, lock, log_flag):
    print(f"From process log, recieved {mem_name}")

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=car_type, buffer=shared_container.buf)

    #todo: once I have the flashdrive, create a permanent mount point
    file_path = "/mnt/logUSB"

    while True:
        time.sleep(1)
        with lock: 
            toSave = pd.DataFrame(data)
            toSave["time"] = datetime.now.strftime("%H:%M:%S")

        if os.path.exists(file_path):
            try:
                toSave.to_csv(file_path + "/log.csv", mode='a', index=False, header=False)
            except Exception as e:
                if log_flag == 1:
                    with open("/mnt/logUSB/log.txt", "a") as file:
                        print(f"{e}\n", file=file) 
                break
            except KeyboardInterrupt:
                break
        else:
            try:
                toSave.to_csv(file_path + "/log.csv", mode='a', index=False, header=True)     #if the file does not exist in the drive, append with the column names
            except Exception as e:
                if log_flag == 1:
                    with open("/mnt/logUSB/log.txt", "a") as file:
                        print(f"{e}\n", file=file) 
                break
            except KeyboardInterrupt:
                break

    shared_container.close()
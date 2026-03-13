import time
from multiprocessing import shared_memory
import numpy as np
import pandas as pd
import os

def run(mem_name, type, lock):
    print(f"From process log, recieved {mem_name}")

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=type, buffer=shared_container.buf)

    #todo: once I have the flashdrive, create a permanent mount point
    filePath = "dummy\path\to\drive"

    while True:
        time.sleep(2)       #every 2 seconds, log
        with lock: 
            toSave = pd.Dataframe(data)

            if os.path.exists(filePath):
                try:
                    toSave.to_csv(filePath, mode='a', index=False, header=False)
                except Exception as e:
                    with open("log.txt", "a") as file:
                        print(f"{e}\n", file=file)
                    break
            else:
                try:
                    toSave.to_csv(filePath, mode='a', index=False, header=True)     #if the file does not exist in the drive, append with the column names
                except Exception as e:
                    with open("log.txt", "a") as file:
                        print(f"{e}\n", file=file)
                    break

    shared_container.close()
    shared_container.unlink()
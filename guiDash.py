from multiprocessing import shared_memory
import numpy as np
import pandas as pd
import time
import can
import os

def run(mem_name, car_type, lock):

    print("Starting GUI")

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=car_type, buffer=shared_container.buf)

    while True:

        try:

            time.sleep(5)

            with lock:
                to_print = pd.DataFrame(data.copy())
        
            print(to_print)

        except Exception as e:
            with open("log.txt", "a") as file:
                print(f"{e}\n", file=file)
            break

        except KeyboardInterrupt:
            break


    shared_container.close()
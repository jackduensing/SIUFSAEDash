from multiprocessing import shared_memory
import numpy as np
import time
import can
import os

def run(mem_name, type):
    print(f"From process GUI, recieved {mem_name}")

    #attaches to shared memory
    car_data = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=type, buffer=car_data.buf)

    time.sleep(3)

    rpm = data['RPM'][0]

    print( f"RPM = {data['RPM'][0]}" )

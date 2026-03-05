from multiprocessing import shared_memory
import numpy as np
import time
import can
import os

def run(mem_name, type):
    print(f"From process can, recieved {mem_name}")

    #attaches to shared memory
    data = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    name = np.ndarray(shape=(1,), dtype=type, buffer=data.buf)

    name['RPM'] = 5000.00
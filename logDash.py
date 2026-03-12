import os
from multiprocessing import shared_memory
import numpy as np

def run(mem_name, type, lock):
    print(f"From process log, recieved {mem_name}")

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=type, buffer=shared_container.buf)

    shared_container.close()
    shared_container.unlink()
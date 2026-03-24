import os
from multiprocessing import shared_memory
import numpy as np
import board
import busio
import digitalio
import adafruit_rfm9x
import time

def run(mem_name, type, lock):
    print(f"From process lora, recieved {mem_name}")

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=type, buffer=shared_container.buf)

    cs = digitalio.DigitalInOut(board.D18)
    reset = digitalio.DigitalInOut(board.D25)
    freq = 915.0

    spi = busio.SPI(clock=board.D21, MOSI=board.D20 , MISO=board.D19)

    lora = adafruit_rfm9x.RFM9x(spi, cs, reset, freq)

    while True:

        time.sleep(1)

        with lock:
            try:
                lora.send(data)
            except Exception as e:
                with open("log.txt", "a") as file:
                    print(f"{e}\n", file=file)
                break

    

    shared_container.close()

    
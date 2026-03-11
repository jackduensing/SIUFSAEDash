import os
from multiprocessing import shared_memory, Process
import numpy as np
import time

import can
import gui
import log
import lora
'''
CAN Fields from car, not exhaustive but complete

Runtime
Manifold Air Pressure
RPM
Coolant Temp
Throttle Position
Manifold Air Temp
Spark Advance
Air Fuel Ratio Target
Air Fuel Ratio
Battery Voltage
Vehicle Speed           #not able
GPS Coordinates         #not able
'''

#names from dbc file

car_data_type = np.dtype([
    ('runtime', np.float32),   #runtime in seconds 
    ('rpm', np.float32),   #RPM
    ('clt', np.float32),   #Coolant Temp
    ('map', np.float32),   #MAP
    ('mat', np.float32),   #MAT
    ('tps', np.float32),   #Throttle Pos
    ('adv_deg', np.float32),   #Spark Advance
    ('afrtgt1', np.float32),   #AFR target
    ('AFR1', np.float32),   #AFR
    ('batt', np.float32),   #Battery Voltage
    ('timestamp', np.float64)
])

mem_name = 'car_data'

car_data = shared_memory.SharedMemory(create=True, size=car_data_type.itemsize, name=mem_name)

#usage for shared data
'''
create array that views the data

name = np.ndarray(shape=(1,), dtype=car_data_type, buffer=car_data.buf)
shape=(1,) means one row
dtype defines data type as the specific array
buffer=car_data.buf points to the 

then can access with name[field]
after locking to prevent race
'''

can = Process(target=can.run, args=(mem_name, car_data_type))
gui = Process(target=gui.run, args=(mem_name, car_data_type))
#log = Process(target=log.run, args=(mem_name, car_data_type))
#lora = Process(target=lora.run, args=(mem_name, car_data_type))

can.start()
gui.start()
#log.start()
#lora.start()



can.join()
gui.join()
#log.join()
#lora.join()



car_data.close()
car_data.unlink()

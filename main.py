import os
from multiprocessing import shared_memory, Process, Lock
import numpy as np
import time

import canDash
import guiDash
import logDash
import loraDash

#names from dbc file

car_data_type = np.dtype([
    ('timestamp', np.float64),
    ('start_time', np.float32),   #holder for timestamping
    ('rpm', np.float32),   #RPM
    ('clt', np.float32),   #Coolant Temp
    ('map', np.float32),   #MAP
    ('mat', np.float32),   #MAT
    ('tps', np.float32),   #Throttle Pos
    ('adv_deg', np.float32),   #Spark Advance
    ('afrtgt1', np.float32),   #AFR target
    ('AFR1', np.float32),   #AFR
    ('batt', np.float32)   #Battery Voltage
])

mem_name = 'car_data'

shared_container = shared_memory.SharedMemory(create=True, size=car_data_type.itemsize, name=mem_name)

data = np.ndarray(shape=(1,), dtype=type, buffer=shared_container.buf)

data['start_time'] = time.monotonic()       #starts the timestampign process, NOTE: only works in comparison to other time.monotonic

lock = Lock()

can = Process(target=canDash.run, args=(mem_name, car_data_type, lock))
gui = Process(target=guiDash.run, args=(mem_name, car_data_type, lock))
#log = Process(target=logDash.run, args=(mem_name, car_data_type, lock))
#lora = Process(target=loraDash.run, args=(mem_name, car_data_type, lock))

can.start()
gui.start()
#log.start()
#lora.start()



can.join()
gui.join()
#log.join()
#lora.join()



shared_container.close()
shared_container.unlink()

#usage for shared data
'''

#attach to the shared container
shared_container = shared_memory.SharedMemory(name = mem_name)

#create the holding arrray that uses the shared container
data = np.ndarray(shape=(1,), dtype=type, buffer=shared_container.buf)

then can access with name[field]
ex:     #data['RPM'] = 5000.00'
assignment to vars with
ex:     #rpm = data['RPM'][0]
after locking to prevent race
'''

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

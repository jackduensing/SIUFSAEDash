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
    ('seconds', np.int32),   #seconds ECU has been on
    ('rpm', np.float32),   #RPM
    ('clt', np.float32),   #Coolant Temp
    ('map', np.float32),   #MAP
    ('mat', np.float32),   #MAT
    ('tps', np.float32),   #Throttle Pos
    ('adv_deg', np.float32),   #Spark Advance
    ('afrtgt1', np.float32),   #AFR target
    ('AFR1', np.float32),   #AFR
    ('batt', np.float32),   #Battery Voltage
    ('gear', np.int32)    #gear indicator
])

mem_name = 'car_data'

shared_container = shared_memory.SharedMemory(create=True, size=car_data_type.itemsize, name=mem_name)

data = np.ndarray(shape=(1,), dtype=car_data_type, buffer=shared_container.buf)

lock = Lock()

canDash = Process(target=canDash.run, args=(mem_name, car_data_type, lock))
guiDash = Process(target=guiDash.run, args=(mem_name, car_data_type, lock))
#logDash = Process(target=logDash.run, args=(mem_name, car_data_type, lock))
#loraDash = Process(target=loraDash.run, args=(mem_name, car_data_type, lock))


print("Starting Processes")
canDash.start()
guiDash.start()
#logDash.start()
#loraDash.start()


try:
    canDash.join()
    guiDash.join()
    #logDash.join()
    #loraDash.join()
except KeyboardInterrupt:
    canDash.terminate()
    guiDash.terminate()
    #logDash.terminate()
    #loraDash.terminate()
    canDash.join()
    guiDash.join()
    #logDash.join()
    #loraDash.join()




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

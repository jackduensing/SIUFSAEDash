from multiprocessing import shared_memory
import numpy as np
import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QTimer, QObject, pyqtSignal, pyqtProperty

class Backend(QObject):

    rpmChanged = pyqtSignal(int, arguments=['RPM'])
    cltChanged = pyqtSignal(int, arguments=['clt'])
    mapChanged = pyqtSignal(int, arguments=['map'])
    matChanged = pyqtSignal(int, arguments=['mat'])
    tpsChanged = pyqtSignal(int, arguments=['tps'])
    adv_degChanged = pyqtSignal(int, arguments=['adv_deg'])
    afrtgt1Changed = pyqtSignal(int, arguments=['afrtgt1'])
    afrChanged = pyqtSignal(int, arguments=['AFR1'])
    battChanged = pyqtSignal(float, arguments=['batt'])
    gearChanged = pyqtSignal(int, arguments=['gear'])

    def __init__(self, data, lock):
        super().__init__()
        self._data = data
        self._lock = lock
        self._rpm = 0
        self._clt = 0
        self._map = 0
        self._mat = 0
        self._tps = 0
        self._adv_deg = 0
        self._afrtgt1 = 0
        self._afr = 0
        self._batt = 0
        self._gear = 0

        self._last_rpm = 0
        self._last_clt = 0
        self._last_map = 0
        self._last_mat = 0
        self._last_tps = 0
        self._last_adv_deg = 0
        self._last_afrtgt1 = 0
        self._last_afr = 0
        self._last_batt = 0
        self._last_gear = 0

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._poll)
        self._timer.start(100)

    def _poll(self):
        with self._lock:
            rpm = float(self._data[0]["rpm"])
            clt = float(self._data[0]["clt"])
            map_ = float(self._data[0]["map"])
            mat = float(self._data[0]["mat"])
            tps = float(self._data[0]["tps"])
            adv_deg = float(self._data[0]["adv_deg"])
            afrtgt1 = float(self._data[0]["afrtgt1"])
            afr = float(self._data[0]["AFR1"])
            batt = float(self._data[0]["batt"])
            gear = float(self._data[0]["gear"])

        if abs(rpm - self._last_rpm) > 1e-3:
            self._last_rpm = rpm
            self._rpm = int(round(rpm))
            self.rpmChanged.emit(rpm)

        if abs(clt - self._last_clt) > 1e-3:
            self._last_clt = clt
            self._clt = int(round(clt))
            self.cltChanged.emit(clt)

        if abs(map_ - self._last_map) > 1e-3:
            self._last_map = map_
            self._map = int(round(map_))
            self.mapChanged.emit(map_)

        if abs(mat - self._last_mat) > 1e-3:
            self._last_mat = mat
            self._mat = int(round(mat))
            self.matChanged.emit(mat)

        if abs(tps - self._last_tps) > 1e-3:
            self._last_tps = tps
            self._tps = int(round(tps))
            self.tpsChanged.emit(tps)

        if abs(adv_deg - self._last_adv_deg) > 1e-3:
            self._last_adv_deg = adv_deg
            self._adv_deg = int(round(adv_deg))
            self.adv_degChanged.emit(adv_deg)

        if abs(afrtgt1 - self._last_afrtgt1) > 1e-3:
            self._last_afrtgt1 = afrtgt1
            self._afrtgt1 = int(round(afrtgt1))
            self.afrtgt1Changed.emit(afrtgt1)

        if abs(afr - self._last_afr) > 1e-3:
            self._last_afr = afr
            self._afr = int(round(afr))
            self.afrChanged.emit(afr)

        if abs(batt - self._last_batt) > 1e-3:
            self._last_batt = batt
            self._batt = int(round(batt))
            self.battChanged.emit(batt)

        if abs(gear - self._last_gear) > 1e-3:
            self._last_gear = gear
            self._gear = int(round(gear))
            self.gearChanged.emit(gear)


    @pyqtProperty(int, notify=rpmChanged)
    def rpm(self):
        return self._rpm
    
    @pyqtProperty(int, notify=cltChanged)
    def clt(self):
        return self._clt
    
    @pyqtProperty(int, notify=mapChanged)
    def map(self):
        return self._map

    @pyqtProperty(int, notify=matChanged)
    def mat(self):
        return self._mat
    
    @pyqtProperty(int, notify=tpsChanged)
    def tps(self):
        return self._tps
    
    @pyqtProperty(int, notify=adv_degChanged)
    def adv_deg(self):
        return self._adv_deg
    
    @pyqtProperty(int, notify=afrtgt1Changed)
    def afrtgt1(self):
        return self._afrtgt1

    @pyqtProperty(int, notify=afrChanged)
    def afr(self):
        return self._afr

    @pyqtProperty(float, notify=battChanged)

    def batt(self):
        return self._batt
    
    @pyqtProperty(int, notify=gearChanged)
    def gear(self):
        return self._gear
    


def run(mem_name, car_type, lock):

    print("Starting GUI")

    #attaches to shared memory
    shared_container = shared_memory.SharedMemory(name = mem_name)

    #creates an array that mirrors the shared memory
    data = np.ndarray(shape=(1,), dtype=car_type, buffer=shared_container.buf)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend(data, lock)
    engine.rootContext().setContextProperty('backend', backend)

    engine.load('main.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    exit_code = app.exec()
    shared_container.close()
    sys.exit(exit_code)


    
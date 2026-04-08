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
            rpm = self._data[0]["rpm"]
            clt = self._data[0]["clt"]
            map_ = self._data[0]["map"]
            mat = self._data[0]["mat"]
            tps = self._data[0]["tps"]
            adv_deg = self._data[0]["adv_deg"]
            afrtgt1 = self._data[0]["afrtgt1"]
            afr = self._data[0]["AFR1"]
            batt = self._data[0]["batt"]
            gear = self._data[0]["gear"]

        if changed(rpm, self._last_rpm):
            self._last_rpm = rpm
            self._rpm = rpm
            self.RPMChanged.emit(int(rpm))

        if changed(clt, self._last_clt):
            self._last_clt = clt
            self._clt = clt
            self.cltChanged.emit(int(clt))

        if changed(map_, self._last_map):
            self._last_map = map_
            self._map = map_
            self.mapChanged.emit(int(map_))

        if changed(mat, self._last_mat):
            self._last_mat = mat
            self._mat = mat
            self.matChanged.emit(int(mat))

        if changed(tps, self._last_tps):
            self._last_tps = tps
            self._tps = tps
            self.tpsChanged.emit(int(tps))

        if changed(adv_deg, self._last_adv_deg):
            self._last_adv_deg = adv_deg
            self._adv_deg = adv_deg
            self.adv_degChanged.emit(int(adv_deg))

        if changed(afrtgt1, self._last_afrtgt1):
            self._last_afrtgt1 = afrtgt1
            self._afrtgt1 = afrtgt1
            self.afrtgt1Changed.emit(int(afrtgt1))

        if changed(afr, self._last_afr):
            self._last_afr = afr
            self._afr = afr
            self.afrChanged.emit(int(afr))

        if changed(batt, self._last_batt):
            self._last_batt = batt
            self._batt = batt
            self.battChanged.emit(batt)

        if changed(gear, self._last_gear):
            self._last_gear = gear
            self._gear = gear
            self.gearChanged.emit(int(gear))

        def changed(a, b, epsilon=1e-3):
            return abs(a - b) > epsilon

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


    
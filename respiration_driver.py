 
from myqt import QT, mkQApp


import pyqtgraph as pg

import time
import datetime
from collections import OrderedDict

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# sudo chmod a+rw /dev/ttyUSB0


#~ phases = [
    #~ (1., b'\x10', 'start'),
    #~ (2., b'\x20', 'Phase 1'),
    #~ (5., b'\x21', 'Phase 2'),
    #~ (10., b'\x11', 'stop'),
#~ ]


#~ phases = [
    #~ (0., b'\x10', 'Will start'),
    #~ (5., b'\x20', 'Respi standard'),
    #~ (5. + 5*60, b'\x21', 'Respi bouche'),
    #~ (5.+ 7*60, b'\x11', 'stop'),
#~ ]




#~ baudrate = 19200
#~ baudrate = 9600

#~ def test_serial():
    #~ ser = serial.Serial('/dev/ttyUSB0', baudrate) #, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
    #~ print(ser)
    #~ print(ser.name) 
    #~ ser.write(b'hello')
    #~ ser.close()
    
    

#~ label_style = """QLabel { 
        #~ background-color : black; 
        #~ color : white;
        #~ font-size : 50pt;
        #~ qproperty-alignment: AlignCenter;

#~ }"""


def prepapre_signal_OLD(freq1=0.3, freq2=0.4, cycle_duration=120., total_duration=60*10, resp_ratio=0.4, sample_rate=100.):
    sr = sample_rate
    length = int(sr*total_duration)

    speed = 1/cycle_duration
    times = np.arange(length)/sr
    #~ freqs =  (np.sin(np.pi*2*speed*times)+1)/2 *  (f2-f1) + f1
    freqs = (scipy.signal.sawtooth(times * np.pi*1/120., width=0.5)+1)/2. *  (freq2-freq1) + freq1
    
    phase = np.cumsum(freqs/sr)*2*np.pi
    sig = np.sin(phase)
    
    
    return times, sig, freqs


def prepapre_signal(freq1=0.3, freq2=0.4, cycle_duration=120., total_duration=60*10, resp_ratio=0.4, left_pad=2., sample_rate=100.):
    sr = sample_rate
    length = int(sr*total_duration)

    speed = 1/cycle_duration
    times = np.arange(length)/sr
    #~ freqs =  (np.sin(np.pi*2*speed*times)+1)/2 *  (f2-f1) + f1
    freqs = (scipy.signal.sawtooth(times * np.pi*1/120., width=0.5)+1)/2. *  (freq2-freq1) + freq1
    phase = np.cumsum(freqs/sr)*2*np.pi + np.pi*2*(1-resp_ratio)

    x = resp_ratio
    t = phase
    
    N = 30
    
    cnxt = lambda x,n,t : (np.cos(n*t)-np.cos(n*(t+2*np.pi*x)))/((1-x)*x*(np.pi*n)**2.) # Composante n
    sig = np.sum([cnxt(x,n,t) for n in range(1,N)],axis=0) # Somme des composantes de 1 a000
    
    n_pad = int(left_pad*sample_rate)
    if n_pad>0:
        freqs = np.hstack((np.zeros(n_pad, dtype=freqs.dtype), freqs))
        sig = np.hstack((-np.ones(n_pad, dtype=sig.dtype), sig))
        times = np.arange(sig.size)/sr
    
    return times, sig, freqs



def test_moving_sinus():
    times, sig, freqs = prepapre_signal(left_pad=3)
    #~ times, sig2, freqs = prepapre_signal_OLD()
    
    fig, axs = plt.subplots(sharex=True, nrows=3)
    axs[0].plot(times, freqs)
    axs[1].plot(times, sig)
    #~ axs[1].plot(times, sig2, color='r')
    plt.show()




def get_dict_from_group_param(param, cascade = False):
    assert param.type() == 'group'
    d = {}
    for p in param.children():
        if p.type() == 'group':
            if cascade:
                d[p.name()] = get_dict_from_group_param(p, cascade = True)
            continue
        else:
            d[p.name()] = p.value()
    return d


    
class RespirationDriver(QT.QWidget):
    
    annotation_changed = QT.pyqtSignal(object)
    
    def __init__(self, parent=None, show_label=False):
        QT.QWidget.__init__(self, parent=parent)
        
        self.show_label = show_label
        
        #self.resize(800, 600)
        
        self.layout = QT.QVBoxLayout()
        self.setLayout(self.layout)
        
        if show_label:
            self.label = QT.QLabel('')
            self.layout.addWidget(self.label)

        self.graphicsview = pg.GraphicsView()
        self.layout.addWidget(self.graphicsview)

        self.plot = pg.PlotItem()
        self.graphicsview.setCentralItem(self.plot)
        self.plot.vb.disableAutoRange()

        self.plot.showAxis('left', False)
        self.plot.showAxis('bottom', False)
        
        self.timer = QT.QTimer(singleShot=False, interval=50)
        self.timer.timeout.connect(self.refresh)
        
    
    def configure(self, sample_rate=200.,  time_range=6., **kargs):
        if self.timer.isActive():
            print('running')
            return
        
        self.time_range = time_range
        self.sample_rate = sample_rate
        self.kargs = kargs
        self.times, self.sig, self.freqs = prepapre_signal(sample_rate=sample_rate, **kargs)
        
        # '#ff0066' 4.5
        self.plot.clear()
        self.curve = pg.PlotCurveItem(pen=pg.mkPen(cosmetic=True, width=6, color='#a7dc2d'),
                                                    connect='finite', antialias=True)
        self.plot.addItem(self.curve)

        # '#ff9900' 50
        self.scatter = pg.ScatterPlotItem(size=100, pxMode=True, brush='#ff9900')
        self.plot.addItem(self.scatter)
        
        sr = 200.
        #~ self.t_vect = t = np.arange(0,time_range,1/sr)
        #~ self.sig = np.sin(2*np.pi*self.resp_freq*t_vect)
        #~ self.sig = np.sin(2*np.pi*freq*t)

        self.plot.setXRange(0, self.time_range, padding = 0.0)
        self.plot.setYRange(-1, 1, padding = 0.0)
        
        self.annotation_changed.emit(kargs)
        
        self.t0 = time.perf_counter()
        
    
    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()
    
    def refresh(self):

        elapsed = time.perf_counter() - self.t0
        
        ind0 = int(elapsed * self.sample_rate)
        ind1 = int((elapsed+self.time_range) * self.sample_rate)
        
        t_vect = self.times[ind0:ind1]
        sig = self.sig[ind0:ind1]
        
        self.curve.setData(t_vect, sig)
        
        self.plot.setXRange(elapsed, elapsed+self.time_range, padding = 0.0)
        
        s = t_vect.size//2
        self.scatter.setData(x=t_vect[s], y=[sig[s]])
        
        if self.show_label:
            self.label.setText('respiration freq = {:0.2}Hz'.format(self.freqs[ind0+s]))



class RespirationDriverController(QT.QWidget):
    def __init__(self, parent=None, respi_driver=None):
        QT.QWidget.__init__(self, parent=parent)
        
        self.respi_driver = respi_driver

        self.layout = QT.QVBoxLayout()
        self.setLayout(self.layout)
        

        d = [
            {'name': 'freq1', 'type': 'float', 'value' : 0.2},
            {'name': 'freq2', 'type': 'float', 'value' : 0.4},
            {'name': 'cycle_duration', 'type': 'float', 'value' : 120.},
            {'name': 'resp_ratio', 'type': 'float', 'value' : 0.4},
        ]
           
        self.params = pg.parametertree.Parameter.create(name='Params', type='group', children=d)
        self.tree_params = pg.parametertree.ParameterTree()
        self.tree_params.header().hide()
        self.tree_params.setParameters(self.params, showTop=True)
        self.layout.addWidget(self.tree_params)
        
        but = QT.QPushButton('start resp driver')
        self.layout.addWidget(but)
        but.clicked.connect(self.do_start)

        but = QT.QPushButton('stop resp driver')
        self.layout.addWidget(but)
        but.clicked.connect(self.do_stop)
    
    def do_start(self):
        self.respi_driver.stop()
        
        d = get_dict_from_group_param(self.params)
        self.respi_driver.configure(**d)
        
        self.respi_driver.start()
        
    def do_stop(self):
        self.respi_driver.stop()
        




def start_mainwindow():
    app = mkQApp()
    rd = RespirationDriver()
    rd.show()
    rd.configure()
    #~ rd.start()
    
    controller = RespirationDriverController(respi_driver=rd)
    controller.show()
    
    app.exec_()
    



    
    
if __name__ == '__main__':
   #~ test_serial()
   # test_moving_sinus()
    
   start_mainwindow()
   



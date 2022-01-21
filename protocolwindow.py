# -*- coding: utf-8 -*-
import os
import shutil
import datetime
import time

from myqt import QT, mkQApp

from respiration_driver import RespirationDriver


PARALLEL_SLEEP = 0.010

class ProtocolWindow(QT.QWidget):
    def __init__(self, steps, log_name,
                    with_serial=False, serial_port=None,
                    with_parallel=False, parallel_adress=None,

                            parent=None):
        QT.QWidget.__init__(self, parent=parent)
        
        print(log_name)
        assert not os.path.exists(log_name)
        
        self.with_serial = with_serial
        self.with_parallel = with_parallel
        
        if self.with_serial:
            import serial
            baudrate = 9600
            self.serial = serial.Serial(serial_port, baudrate)
        
        if self.with_parallel:
            from psychopy import parallel
            self.port = parallel.ParallelPort(address=parallel_adress)
        
        self.steps = steps
        self.log_name = log_name
        
        # self.resize(800, 600)
        self.showFullScreen()
        
        self.layout = QT.QVBoxLayout()
        self.setLayout(self.layout)
        
        self.label = QT.QLabel(alignment=QT.AlignCenter)
        self.label.setSizePolicy(QT.QSizePolicy.Expanding, QT.QSizePolicy.Expanding)
        self.layout.addWidget(self.label)
        
        self.resp_driver = RespirationDriver()
        self.layout.addWidget(self.resp_driver)
        self.resp_driver.hide()
        
        #~ self.question_slide = QuestionSlide()
        #~ self.layout.addWidget(self.question_slide)
        #~ self.question_slide.hide()
        #~ self.question_slide.done.connect(self.on_question_done)

        self.timer = QT.QTimer(singleShot=True)
        self.timer.timeout.connect(self.next_step)
        
        self.key_enable = False
        self.num_step = -1
        
        with open(self.log_name, mode='w', encoding='utf8')as f :
            f.write('')
    
    def add_log(self, txt):
        with open(self.log_name, mode='a', encoding='utf8') as f :
            f.write(txt)
        
    def start(self):
        self.next_step()
        
    def next_step(self):
        if self.num_step< len(self.steps) and self.steps[self.num_step]['type'] == 'respidriver':
            self.resp_driver.stop()
        
        self.num_step += 1
        
        if self.num_step >= len(self.steps):
            self.label.setText('')
            self.label.show()
            if self.with_serial:
                self.serial.close()
            
            if self.with_parallel:
                # no close port
                pass
            
            return 
        
        step = self.steps[self.num_step]
        
        txt = step.get('text', None)
        
        if txt is not None:
            self.label.setText(txt)
            self.label.show()
        else:
            self.label.hide()
        
        duration = step.get('duration', None)
        if duration is None or duration == 'wait_key':
            self.key_enable = True
        else:
            self.timer.setInterval(int(step['duration']*1000))
            self.timer.start()
            self.key_enable = False
        
        if step['type'] == 'respidriver':
            self.resp_driver.show()
            self.resp_driver.configure(sample_rate=200.,  time_range=6., **step['params'])
            self.resp_driver.start()
        else:
            self.resp_driver.hide()
        
        #~ if step['type'] == 'question':
            #~ self.question_slide.show()
        #~ else:
            #~ self.question_slide.hide()

        if step['type'] == 'question':
            self.question_slide = QuestionSlide()
            self.layout.addWidget(self.question_slide)
            self.question_slide.done.connect(self.on_question_done)
            self.question_slide.start(step['question_list'])
        
        if 'trigger' in step:
            trigger = step['trigger']
            txt = '[Trig {}] [{}]\n'.format(trigger, datetime.datetime.now().isoformat())
            
            self.add_log(txt)
            if self.with_serial:
                paquet = chr(trigger).encode()
                print('paquet', paquet)
                self.serial.write(paquet)
            
            if self.with_parallel:
                from psychopy import parallel
                self.port.setData(int(trigger))
                time.sleep(PARALLEL_SLEEP)
                self.port.setData(0x00)

    def keyPressEvent(self, event):
        if self.key_enable:
            self.next_step()
    
    def on_question_done(self):
        qlist = self.steps[self.num_step]['question_list']
        values = self.question_slide.values
        txt = '[Question {}] [{}]\n'.format(self.num_step, datetime.datetime.now().isoformat())
        for i in range(len(qlist)):
            txt += '    {} : {}\n'.format(qlist[i]['label'], values[i])
        
        self.add_log(txt)
        
        self.question_slide.hide()
        self.layout.removeWidget(self.question_slide)
        self.question_slide = None
        
        self.next_step()


class QuestionSlide(QT.QWidget):
    done = QT.pyqtSignal()
    def __init__(self, parent=None):
        QT.QWidget.__init__(self, parent=parent)
        
        self.layout = QT.QVBoxLayout()
        self.setLayout(self.layout)
        
        self.layout.addStretch()
        self.layout.addStretch()
        
    def start(self, question_list):
        # clear layout
        item = self.layout.takeAt(1)
        while item is not None:
            if item.widget():
                self.layout.removeWidget(item.widget())
            item = self.layout.takeAt(1)
        self.question_list = question_list
        self.sliders = []
        self.values = []
        self.num = -1
        
        self.display_next()
    
    def display_next(self):
        self.num += 1
        
        if self.num >= len(self.question_list):
            self.done.emit()
            return
        
        font_size = 25
        question = self.question_list[self.num]
        
        label = QT.QLabel(question['label'], alignment=QT.AlignCenter)
        font = label.font()
        font.setPointSize(font_size)
        label.setFont(font)

        slider = QT.QSlider(QT.Qt.Horizontal)
        self.sliders.append(slider)
        slider.setValue(50)

        h = QT.QHBoxLayout()
        self.layout.insertWidget(self.num*2+1, label)
        self.layout.insertLayout(self.num*2+2, h)
        
        lelft_label = QT.QLabel(question['left_label'])
        font = lelft_label.font()
        font.setPointSize(font_size)
        lelft_label.setFont(font)

        h.addWidget(lelft_label)
        h.addWidget(slider)
        
        right_label = QT.QLabel(question['right_label'])
        font = right_label.font()
        font.setPointSize(font_size)
        right_label.setFont(font)
        
        h.addWidget(right_label)
        self.layout.addStretch()
        
        slider.setFocus()

    def keyPressEvent(self, event):
        if not self.isVisible():
            # this make event process by ProtocolWindow
            event.ignore()
            return
        
        if self.num >= len(self.question_list):
            event.ignore()
            return
            
        if event.key() == QT.Qt.Key_Space:
            self.values.append(self.sliders[-1].value())
            self.display_next()
            event.accept()



def test_question():
    app = mkQApp()
    
    question_list = [
        {'label': 'Vous êtes', 'left_label' : 'de gauche', 'right_label': 'de droite'},
        {'label': 'Vous aimez', 'left_label' : 'la coquetterie', 'right_label': 'la classe'},
    ]
    
    w = QuestionSlide()
    def on_done():
        print('DONE')
        print(w.values)
    w.done.connect(on_done)

    w.resize(800, 600)
    w.show()
    w.start(question_list)
    app.exec_()
    


def debug_protocolwindow():
    style = """
    <style>
    .container {
        position: relative;
        background-color: #FFFFFF;
        margin: 0;
        height:100%;
    }

    .center {
        margin: 00;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    </style>
    """

    txt1 = """
    <div class="center container ">
            <p style="font-size:50pt">Questionnaire avec question vérif</p>
    </div>
    """

    question_list1 = [
        {'label': 'Vous êtes', 'left_label' : 'de gauche', 'right_label': 'de droite'},
        {'label': 'Vous aimez', 'left_label' : 'la coquetterie', 'right_label': 'la classe'},
    ]


    question_list2 = [
        {'label': 'Vous êtes', 'left_label' : 'de gauche', 'right_label': 'de droite'},
        {'label': 'Vous aimez', 'left_label' : 'la coquetterie', 'right_label': 'la classe'},
    ]


    steps = [
        {'type': 'question', 'question_list': question_list1},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt1, 'trigger' : 1},
        {'type': 'question', 'question_list': question_list2, 'trigger' : 2},
        {'type': 'respidriver', 'duration':5, 'params' : {'freq1' : .15, 'freq2':.2, 'cycle_duration':60, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger' : 3},
        {'type': 'display', 'duration': 'wait_key', 'text' : '', 'trigger' : 4},
    ]

    log_name = 'test_log.txt'
    
    if os.path.exists(log_name):
        os.remove(log_name)
    
    app = mkQApp()
    # w = ProtocolWindow(steps, log_name, with_serial=True)
    w = ProtocolWindow(steps, log_name, with_serial=False)
    w.show()
    w.start()
    app.exec_()

    


def test_trigger_serial():
    # pip install pyserial
    
    import serial
    baudrate = 9600
    serial_port = 'COM6'
    # serial_port = 'COM3'
    
    
    # serial = serial.Serial('/dev/ttyUSB0', baudrate, parity=serial.PARITY_EVEN, rtscts=1) 
    serial = serial.Serial(serial_port, baudrate, parity=serial.PARITY_EVEN, rtscts=1) 
    
    for trigger in [1, 2, 3, 4, 5, 10, 30, 50, 60, 100, 200]:
        paquet = chr(trigger).encode()
        print('paquet', paquet)
        serial.write(paquet)
        time.sleep(1)


def test_trigger_parralel(parallel_adress):
    # import parallel
    # port = parallel.Parallel()  # open LPT1 or /dev/parport0

    # LPT1 : "0x0378"
    # LPT2 : "0xC030"
    from psychopy import parallel
    port = parallel.ParallelPort(address=parallel_adress)
    
    #for trigger in [1, 2, 3, 4, 5, 10, 30, 50, 60, 100, 200]:
    for trigger in [1, 2, 4, 255]:
        print('trigger', trigger)
        port.setData(trigger)
        time.sleep(0.5)
        port.setData(0x00)
        time.sleep(1.0)
        
    
    






if __name__ == '__main__':
    # test_question()
    
    # debug_protocolwindow()
    
    #~ test_trigger_serial()
    test_trigger_parralel()
    
    
    
    
    
    



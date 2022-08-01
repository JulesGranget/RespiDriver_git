from myqt import QT, mkQApp

import sounddevice as sd
import soundfile as sf

class SoundPlayer(QT.QThread):
    sound_finished = QT.pyqtSignal()
    
    def __init__(self, file_path, parent=None):
        QT.QThread.__init__(self, parent=parent)
        self.file_path = file_path
        
        print('SoundPlayer', file_path)
        
        
        
    def run(self):
        data, fs = sf.read(self.file_path, always_2d=True)
        
        sd.play(data, fs)
        sd.wait()
        
        self.sound_finished.emit()
        
        
        
def test_SoundPlayer():
    
    file_path = 'beige.wav'

    app = mkQApp()
    
    
    
    
    sp = SoundPlayer(file_path)
    
    def on_finished():
        print('finished')
    
    sp.sound_finished.connect(on_finished)
    sp.start()
    
    app.exec_()



if __name__ == '__main__':
    test_SoundPlayer()
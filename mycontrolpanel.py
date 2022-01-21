
from idephyx.myqt import QT, mkQApp

import plot_resp_distribution


class ControlPanel(QT.QWidget):
    def __init__(self, parent=None, respi_driver_controller=None):
        QT.QWidget.__init__(self, parent=parent)
        self.layout = QT.QVBoxLayout()
        self.setLayout(self.layout)
        
        
        but = QT.QPushButton('Open freeResp file')
        self.layout.addWidget(but)
        but.clicked.connect(self.open_free_resp_result)
        
        self.rdc = respi_driver_controller
        self.layout.addWidget(self.rdc)
        
        self.figs = []
    
    def open_free_resp_result(self):

        fd = QT.QFileDialog(fileMode=QT.QFileDialog.DirectoryOnly, acceptMode=QT.QFileDialog.AcceptOpen)
        fd.setViewMode( QT.QFileDialog.Detail )
        if not fd.exec_():
            return
            
        dirname = fd.selectedFiles()[0]
        print(dirname)
        
        figs = plot_resp_distribution.analyse_dir(dirname, debug=False)
        
        self.figs.extend(figs)
        for fig in figs:
            fig.show()
        
        
        

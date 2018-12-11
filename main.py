import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ntpath
import os
import curly_braces_remover

class MainDialog(QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        uic.loadUi('CurlyBracesRemoverDialog.ui', self)
        self.pushButton_selectFile.clicked.connect(self.on_pushBtn_selectFile_clicked)
        self.pushButton_rmAndSave.clicked.connect(self.on_pushBtn_rmAndSave_clicked)
        self.filename=''
    
    def on_pushBtn_selectFile_clicked(self):
        self.filename, _fileter = QFileDialog.getOpenFileName()   
        self.lineEdit_inputFile.setText(self.filename)

    def on_pushBtn_rmAndSave_clicked(self):
        if not self.filename:
            QMessageBox.warning(self, 'ERROR', 'You have to select a file.')
            return

        # analysis input file path
        dirname, filename = ntpath.split(self.filename)        
        filename_wo_ext, ext = os.path.splitext(filename)        
        out_filename = dirname + '/' + filename_wo_ext + '_RMBs' + ext
        self.lineEdit_outputFile.setText(out_filename)
        if(curly_braces_remover.remove_curly_brasces(self.filename, out_filename) is True):
            QMessageBox.information(self, 'OK', 'remove and output success')
        else:
            QMessageBox.warning(self, 'NG', 'remove and output failed')

def main():
    app = QtWidgets.QApplication(sys.argv)
    dlg = MainDialog()
    dlg.show()
    sys.exit(app.exec_())    

####### module entry #################
if __name__ == '__main__':
    main()
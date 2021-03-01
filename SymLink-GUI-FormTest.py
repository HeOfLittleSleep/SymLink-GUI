import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout)

class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("SymGen")
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox()
        layout = QFormLayout()
        layout.addRow(QLabel("SymLInk Name"))
        SymName = layout.addRow(QLineEdit())
        layout.addRow(QLabel("Target (where the link will point to)"))
        SymTarget = layout.addRow(QLineEdit())
        layout.addRow(QLabel("Location (where the link will appear)"))
        SymLoc = layout.addRow(QLineEdit())
        self.formGroupBox.setLayout(layout)

    # SymCommand = str('mklink /D "' + SymLoc + '/' + SymName + '" "' + SymTarget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())

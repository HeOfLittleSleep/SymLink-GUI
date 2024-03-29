# Written By Timothy Potter (HeOfLittleSleep) with python 3.9.2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
import os

def on_click(self):
    print("chosen target is  " + SymTargetTxt)
    # os.system("ls")


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SymLinkGen")
        MainWindow.resize(183, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 160, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        SymNameTxt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        SymNameTxt.setObjectName("SymName")
        self.verticalLayout.addWidget(SymNameTxt)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        SymTargetTxt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        SymTargetTxt.setObjectName("SymTarget")
        self.verticalLayout.addWidget(SymTargetTxt)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        SymLocTxt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        SymLocTxt.setObjectName("SymLoc")
        self.verticalLayout.addWidget(SymLocTxt)

        GenLinkBtn = QtWidgets.QPushButton(self.centralwidget)
        GenLinkBtn.setGeometry(QtCore.QRect(10, 180, 158, 23))
        GenLinkBtn.setObjectName("BtnGenLink")
        GenLinkBtn.setText("Generate SymLink")
        GenLinkBtn.clicked.connect(on_click)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 183, 21))
        self.menubar.setObjectName("menubar")
        self.menuSymLink_generator = QtWidgets.QMenu(self.menubar)
        self.menuSymLink_generator.setObjectName("menuSymLink_generator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSymLink_generator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SymLink Generator"))
        self.label.setText(_translate("MainWindow", "SymLink Name"))
        self.label_2.setText(_translate("MainWindow", "SymLink Target"))
        self.label_3.setText(_translate("MainWindow", "SymLink Location"))
        # GenLinkBtn.setText(_translate("MainWindow", "Generate SymLink"))
        self.menuSymLink_generator.setTitle(_translate("MainWindow", "SymLink Generator"))

#actually displays the main window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

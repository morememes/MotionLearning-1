from Dialogs import *
from Settings import *
from Algo import *
from PyQt5 import QtCore, QtWidgets


class ConvThA(QtCore.QThread):
    """ потом отвечающий за коннвертацию аудио фреймов """
    def __init__(self, gui, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.gui = gui
        self.isRun = False

    def run(self):
        AudioConv(self, self.gui)  # Старт функции обработки


class ConvTh(QtCore.QThread):
    """ потом отвечающий за коннвертацию фреймов """
    ProgressBarSignal = QtCore.pyqtSignal(float)
    StatusBarSignal = QtCore.pyqtSignal(str)

    def __init__(self, gui, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.gui = gui

    def run(self):
        MLConv(self, self.gui) # Старт функции обработки


# =====================================================================================================================
#
# Gui classes
#
# =====================================================================================================================


class DAbout(QtWidgets.QDialog):
    """ Окно About """
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)


class DSavePath(QtWidgets.QDialog):
    """ Окно Save Path """
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent, QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_SaveDialog()
        self.ui.setupUi(self)


class tabSettings(QtWidgets.QTabWidget):
    """ Окно с настройками """
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self)
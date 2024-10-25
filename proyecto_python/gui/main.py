from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from gui.registro import RegistroWindow

class MainWindow():
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        self.initGUI()
        self.main.showMaximized()

    def initGUI(self):
        self.main.btnRegistrarTransferencias.triggered.connect(self.abrirRegistro)

    def abrirRegistro(self):
        self.registro = uic.loadUi("gui/registro.ui")
        self.registro.show()
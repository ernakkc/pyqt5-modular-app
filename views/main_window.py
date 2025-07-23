from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from controllers.main_controller import MainController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/main_window.ui", self)
        self.controller = MainController(self)
        self.init_ui()

    def init_ui(self):
        self.pushButton.clicked.connect(self.controller.say_hello)

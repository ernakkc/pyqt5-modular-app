from PyQt5.QtWidgets import QMessageBox

class MainController:
    def __init__(self, view):
        self.view = view

    def say_hello(self):
        QMessageBox.information(self.view, "Merhaba", "Merhaba PyQt5!")

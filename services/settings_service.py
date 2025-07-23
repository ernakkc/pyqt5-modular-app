from PyQt5.QtCore import QSettings

class SettingsService:
    def __init__(self):
        self.settings = QSettings("MyCompany", "MyApp")

    def save(self, key, value):
        self.settings.setValue(key, value)

    def load(self, key, default=None):
        return self.settings.value(key, default)

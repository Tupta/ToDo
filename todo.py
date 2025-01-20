#!python

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QInputDialog
from gui_z0 import Ui_Widget

class Task(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Task, self).__init__(parent)
        self.setupUi(self)

        self.logujBtn.clicked.connect(self.loguj)
        self.koniecBtn.clicked.connect(self.koniec)

    def loguj(self):
        login, ok = QInputDialog.getText(self, "Zaloguj się", "Podaj login:")
        if ok:
            if not login or not haslo:
                QMessageBox.warning(self, "Błąd", 'Puty login lub hasło', QMessageBox.ok)
                return
            QMessageBox.information(self, "Dane logowania", "Podano" + login +' ' + haslo, QMessageBox.Ok)
            
    def koniec(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Task()
    window.show()
    sys.exit(app.exec_())
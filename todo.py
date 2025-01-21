#!python

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QInputDialog
from gui import Ui_Widget, LoginDialog

class Task(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Task, self).__init__(parent)
        self.setupUi(self)

        self.logujBtn.clicked.connect(self.loguj)
        self.koniecBtn.clicked.connect(self.koniec)

    def loguj(self):
        login, haslo, ok = LoginDialog.getLoginHaslo(self)
        if not ok:
            return
        
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
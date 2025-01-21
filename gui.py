#!python

from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel, QLineEdit, QGridLayout 
from PyQt5.QtCore import Qt

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
       
        # Tabelaryczny widok danych
        self.widok = QTableView()
    
        # Przyciski PUSH
        self.logujBtn = QPushButton("Za&loguj", Widget)
        self.koniecBtn = QPushButton("&Koniec", Widget)

        # Układ przycisków PUSH
        uklad = QHBoxLayout()
        uklad.addWidget(self.logujBtn)
        uklad.addWidget(self.koniecBtn)
    
        # Układ całego okna
        ukladV = QVBoxLayout()
        ukladV.addWidget(self.widok)
        ukladV.addLayout(uklad)
        Widget.setLayout(ukladV)  # Przypisanie układu do głównego widżetu
    
        # Właściwości widżetu
        Widget.setWindowTitle("Lista zadań")
        Widget.resize(800, 600)

class LoginDialog(QDialog):
    #Okno dialogowe logowania
    
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        
        #etykiety pola edycji i i przyciski
        loginLbl = QLabel('Login')
        hasloLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.przyciski = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, QtHorizontal, self)
        
        #układ główny okna (rozmieszczenie)
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(hasloLbl, 1, 0)
        uklad.addWidget(hasloLbl, 1, 1)
        uklad.addWidget(self.przyciski, 2, 0, 2, 0)
        
        # sygnały i sloty
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)
        
        #własciwosci widgetu
        self.setModal(True) #przy otwartym oknie nie mozna klikac w inne okna
        self.setWindowTitle('Logowanie') 
        
    def loginHaslo(self):
        return (self.login.text().strip(), 
                self.haslo.text().strip())
        
    #metoda statyczna tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = LoginDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login, haslo = dialog.loginHaslo()
        return (login, haslo, ok == QDialog.Accepted)
        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Widget = QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

#!python

from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QPushButton, QHBoxLayout, QVBoxLayout


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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Widget = QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
window = QMainWindow()
layout = QVBoxLayout()
def DoPrimary():
    import Main
window.setWindowTitle("MathsWatch Bot")
window.setGeometry(0, 0, 500, 500)
# layout.addWidget(QLabel("Bot"), 0, 0)
primarybutton = QPushButton("Start Primary questions")
primarybutton.clicked.connect(DoPrimary)
layout.addWidget(primarybutton)
widget = QWidget()
widget.setLayout(layout)


window.setMenuWidget(widget)
window.show()
app.exec()

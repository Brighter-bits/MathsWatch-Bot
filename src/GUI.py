from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QIcon
import ctypes

def DoPrimary():
    #This is the function which will Start the bot, currently there is only Primary
    with open('Global Variables.txt', 'w') as f:
        #Stores the Username and Password in a plain text file (Kinda bad security, although I'm not sure how you could encrypt this)
        #This means that Driver can take the Username and Password without importing GUI
        #It also means that you won't have to reenter your username and password after restarting
        f.write(UsernameBox.text().strip("\n"))
        f.write("\n")
        f.write(PasswordBox.text().strip("\n"))
        f.close()
    import Main
    Main.Primary()

def CreateWindow():
    app = QApplication([])
    window = QMainWindow()
    layout = QVBoxLayout()
    global UsernameBox
    global PasswordBox
    try:
        with open('Global Variables.txt', 'r') as f:
            Memory = f.readlines()
            f.close()
        UsernameBox = QLineEdit()
        UsernameBox.setText(Memory[0].strip("\n"))
        UsernameBox.setPlaceholderText("Username")

        PasswordBox = QLineEdit()
        PasswordBox.setText(Memory[1].strip("\n"))
        PasswordBox.setPlaceholderText("Password")
        PasswordBox.setEchoMode(QLineEdit.EchoMode.Password)
        
    except:
        UsernameBox = QLineEdit()
        UsernameBox.setPlaceholderText("Username")

        PasswordBox = QLineEdit()
        PasswordBox.setPlaceholderText("Password")
        PasswordBox.setEchoMode(QLineEdit.EchoMode.Password)
        #Creates Username and Password Input boxes

    window.setWindowTitle("MathsWatch Bot")
    window.setGeometry(0, 0, 500, 500)
    window.setWindowIcon(QtGui.QIcon('src\BB.ico'))
    widgets = []
    # layout.addWidget(QLabel("Bot"), 0, 0)
    primarybutton = QPushButton("Start Primary questions")
    primarybutton.clicked.connect(DoPrimary)
    
    myappid = 'mycompany.myproduct.subproduct.version' 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) #This just makes the taskbar icon the same as the app icon

    #Puts all of these values into a list
    widgets.append(UsernameBox)
    widgets.append(PasswordBox)
    widgets.append(primarybutton)


    for bob in range(len(widgets)):
        layout.addWidget(widgets[bob])
        #add each widget into the layout
    widget = QWidget()
    widget.setLayout(layout)

    window.setMenuWidget(widget)
    window.show()
    app.exec()
CreateWindow()
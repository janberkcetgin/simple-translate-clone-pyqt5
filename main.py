import sys
from PyQt5.QtWidgets import *


from translate_ui import *
from translate import Translator

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()

def translate1():
    _Qcombobox1 = ui.comboBox.currentText()
    _Qcombobox2 = ui.comboBox_2.currentText()
    _LineEdit1 = ui.plainTextEdit.toPlainText()


    translator = Translator(from_lang=_Qcombobox1,
                            to_lang=_Qcombobox2)
    ui.textEdit.setText(translator.translate(_LineEdit1))

def change():
    x = ui.comboBox.currentText()
    y = ui.comboBox_2.currentText()
    ui.comboBox.setCurrentText(y)
    ui.comboBox_2.setCurrentText(x)

def copy():
    ui.textEdit.selectAll()
    ui.textEdit.copy()
    ui.statusbar.showMessage("Copied",3000)


ui.pushButton_change.clicked.connect(change)
ui.pushButton.clicked.connect(translate1)
ui.pushButton_copy.clicked.connect(copy)



sys.exit(app.exec_())


__version__ = 1.0
print(__version__, type(__version__))

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from ui import Ui_Form

class Operation(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # isInt = isinstance(x, int)
        self.addButton.clicked.connect(self.addOperand)
        self.subButton.clicked.connect(self.subOperand)
        self.pushButton_3.clicked.connect(self.clearOutputs)

    def addOperand(self):
        # self.n1 = self.num1.text()
        # self.n2 = self.num2.text()
        self.label_5.setText(" ")
        try:
            # print(self.num1.text())
            self.sum = int(self.num1.text()) + int(self.num2.text())
            self.addOutput.setText(str(self.sum))
        except:
            print("Enter Integer Value Only")
            self.label_5.setText("Enter Integer Value Only")
    def clearOutputs(self):
        self.addOutput.setText('')
    def addOperand(self):
        # self.n1 = self.num1.text()
        # self.n2 = self.num2.text()
        self.label_5.setText(" ")
        try:
            # print(self.num1.text())
            self.sum = int(self.num1.text()) + int(self.num2.text())
            self.addOutput.setText(str(self.sum))
        except:
            print("Enter Integer Value Only")
            self.label_5.setText("Enter Integer Value Only")
        
    def subOperand(self):
        # self.n1 = self.num1.text()
        # self.n2 = self.num2.text()
        self.label_5.setText(" ")
        try:
            # print(self.num1.text())
            self.sub = int(self.num1.text()) - int(self.num2.text())
            self.subOutput.setText(str(self.sub))
        except:
            print("Enter Integer Value Only")
            self.label_5.setText("Enter Integer Value Only")

          
    def clearOutputs(self):
        self.addOutput.setText('')
        self.subOutput.setText('')
        
if __name__ == "__main__":
    import sys
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Operation()
    window.show()
    sys.exit(app.exec_())  
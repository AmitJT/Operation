# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(313, 416)
        Form.setMinimumSize(QtCore.QSize(313, 416))
        Form.setMaximumSize(QtCore.QSize(313, 416))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(30, 0))
        self.label_3.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMinimumSize(QtCore.QSize(30, 0))
        self.label_4.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 0, 2, 1, 1)
        self.num2 = QtWidgets.QLineEdit(self.widget_2)
        self.num2.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num2.setFont(font)
        self.num2.setAlignment(QtCore.Qt.AlignCenter)
        self.num2.setObjectName("num2")
        self.gridLayout_3.addWidget(self.num2, 0, 6, 1, 1)
        self.num1 = QtWidgets.QLineEdit(self.widget_2)
        self.num1.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num1.setFont(font)
        self.num1.setAlignment(QtCore.Qt.AlignCenter)
        self.num1.setObjectName("num1")
        self.gridLayout_3.addWidget(self.num1, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 5)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        self.subButton = QtWidgets.QPushButton(self.widget_3)
        self.subButton.setObjectName("subButton")
        self.gridLayout_4.addWidget(self.subButton, 2, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.widget_3)
        self.addButton.setObjectName("addButton")
        self.gridLayout_4.addWidget(self.addButton, 1, 0, 1, 1)
        self.subOutput = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.subOutput.setFont(font)
        self.subOutput.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.subOutput.setText("")
        self.subOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.subOutput.setObjectName("subOutput")
        self.gridLayout_4.addWidget(self.subOutput, 2, 1, 1, 1)
        self.addOutput = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addOutput.setFont(font)
        self.addOutput.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.addOutput.setText("")
        self.addOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.addOutput.setObjectName("addOutput")
        self.gridLayout_4.addWidget(self.addOutput, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 4, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.widget_3, 5, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 5)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 5)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Num1"))
        self.label_4.setText(_translate("Form", "Num2"))
        self.subButton.setText(_translate("Form", "SUBTRACT"))
        self.addButton.setText(_translate("Form", "ADD"))
        self.pushButton_3.setText(_translate("Form", "CLEAR OUTPUT"))
        self.label.setText(_translate("Form", "Operation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

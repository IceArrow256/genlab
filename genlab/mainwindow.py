# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genlab/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_work_purpose = QtWidgets.QLabel(self.central_widget)
        self.label_work_purpose.setObjectName("label_work_purpose")
        self.gridLayout.addWidget(self.label_work_purpose, 6, 0, 1, 1)
        self.label_work_theme = QtWidgets.QLabel(self.central_widget)
        self.label_work_theme.setObjectName("label_work_theme")
        self.gridLayout.addWidget(self.label_work_theme, 5, 0, 1, 1)
        self.label_subjects = QtWidgets.QLabel(self.central_widget)
        self.label_subjects.setObjectName("label_subjects")
        self.gridLayout.addWidget(self.label_subjects, 3, 0, 1, 1)
        self.combo_box_subjects = QtWidgets.QComboBox(self.central_widget)
        self.combo_box_subjects.setObjectName("combo_box_subjects")
        self.gridLayout.addWidget(self.combo_box_subjects, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(579, 66, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 2)
        self.spin_box = QtWidgets.QSpinBox(self.central_widget)
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(18)
        self.spin_box.setObjectName("spin_box")
        self.gridLayout.addWidget(self.spin_box, 1, 1, 1, 1)
        self.combo_box_teacher_name = QtWidgets.QComboBox(self.central_widget)
        self.combo_box_teacher_name.setObjectName("combo_box_teacher_name")
        self.gridLayout.addWidget(self.combo_box_teacher_name, 4, 1, 1, 1)
        self.text_edit_work_purpose = QtWidgets.QTextEdit(self.central_widget)
        self.text_edit_work_purpose.setObjectName("text_edit_work_purpose")
        self.gridLayout.addWidget(self.text_edit_work_purpose, 6, 1, 1, 1)
        self.label_conclusion = QtWidgets.QLabel(self.central_widget)
        self.label_conclusion.setObjectName("label_conclusion")
        self.gridLayout.addWidget(self.label_conclusion, 7, 0, 1, 1)
        self.push_button_process = QtWidgets.QPushButton(self.central_widget)
        self.push_button_process.setObjectName("push_button_process")
        self.gridLayout.addWidget(self.push_button_process, 9, 0, 1, 2)
        self.label_number = QtWidgets.QLabel(self.central_widget)
        self.label_number.setObjectName("label_number")
        self.gridLayout.addWidget(self.label_number, 1, 0, 2, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 1)
        self.text_edit_conclusion = QtWidgets.QTextEdit(self.central_widget)
        self.text_edit_conclusion.setObjectName("text_edit_conclusion")
        self.gridLayout.addWidget(self.text_edit_conclusion, 7, 1, 1, 1)
        self.label_teacher_name = QtWidgets.QLabel(self.central_widget)
        self.label_teacher_name.setObjectName("label_teacher_name")
        self.gridLayout.addWidget(self.label_teacher_name, 4, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.central_widget)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.line_edit_name = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_name.setObjectName("line_edit_name")
        self.gridLayout.addWidget(self.line_edit_name, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GenLab"))
        self.label_work_purpose.setText(_translate("MainWindow", "<html><head/><body><p>Work purpose:</p></body></html>"))
        self.label_work_theme.setText(_translate("MainWindow", "Work theme:"))
        self.label_subjects.setText(_translate("MainWindow", "Subjects:"))
        self.label_conclusion.setText(_translate("MainWindow", "Conclusion:"))
        self.push_button_process.setText(_translate("MainWindow", "Process"))
        self.label_number.setText(_translate("MainWindow", "Number:"))
        self.label_teacher_name.setText(_translate("MainWindow", "Teacher name:"))
        self.label_name.setText(_translate("MainWindow", "Name"))

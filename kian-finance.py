# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kian-finance.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 6, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 7, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 8, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.clothesLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.clothesLineEdit.setObjectName("clothesLineEdit")
        self.gridLayout_2.addWidget(self.clothesLineEdit, 9, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 10, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 10, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 8, 1, 1, 1)
        self.clothesLabel = QtWidgets.QLabel(self.tab_2)
        self.clothesLabel.setObjectName("clothesLabel")
        self.gridLayout_2.addWidget(self.clothesLabel, 9, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 12, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 13, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 11, 0, 1, 2)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 12, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 15, 0, 1, 2)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 13, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 14, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 14, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(80, 0, 641, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 10, 855, 540))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_3.addWidget(self.lineEdit_24, 14, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 11, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 14, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget_3)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_3.addWidget(self.dateEdit, 11, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 7, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 8, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 4, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 6, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 10, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 13, 0, 1, 3)
        self.clothesLabel_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.clothesLabel_2.setObjectName("clothesLabel_2")
        self.gridLayout_3.addWidget(self.clothesLabel_2, 9, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 17, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 18, 0, 1, 3)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_3.addWidget(self.lineEdit_27, 17, 1, 1, 2)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_3.addWidget(self.lineEdit_22, 10, 1, 1, 2)
        self.clothesLineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.clothesLineEdit_2.setObjectName("clothesLineEdit_2")
        self.gridLayout_3.addWidget(self.clothesLineEdit_2, 9, 1, 1, 2)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_3.addWidget(self.lineEdit_15, 4, 1, 1, 2)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_3.addWidget(self.lineEdit_16, 5, 1, 1, 2)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_3.addWidget(self.lineEdit_23, 8, 1, 1, 2)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_3.addWidget(self.lineEdit_20, 7, 1, 1, 2)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_3.addWidget(self.lineEdit_18, 6, 1, 1, 2)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_3.addWidget(self.lineEdit_17, 2, 1, 1, 2)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_3.addWidget(self.lineEdit_14, 3, 1, 1, 2)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_3.addWidget(self.lineEdit_19, 0, 1, 1, 2)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_3.addWidget(self.lineEdit_21, 1, 1, 1, 2)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 12, 0, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_3.addWidget(self.lineEdit_26, 12, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_5)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 40, 591, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 10, 855, 540))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_3.addWidget(self.lineEdit_24, 14, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 11, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 14, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget_3)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_3.addWidget(self.dateEdit, 11, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 7, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 8, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 4, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 6, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 10, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 13, 0, 1, 3)
        self.clothesLabel_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.clothesLabel_2.setObjectName("clothesLabel_2")
        self.gridLayout_3.addWidget(self.clothesLabel_2, 9, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 17, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 18, 0, 1, 3)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_3.addWidget(self.lineEdit_27, 17, 1, 1, 2)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_3.addWidget(self.lineEdit_22, 10, 1, 1, 2)
        self.clothesLineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.clothesLineEdit_2.setObjectName("clothesLineEdit_2")
        self.gridLayout_3.addWidget(self.clothesLineEdit_2, 9, 1, 1, 2)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_3.addWidget(self.lineEdit_15, 4, 1, 1, 2)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_3.addWidget(self.lineEdit_16, 5, 1, 1, 2)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_3.addWidget(self.lineEdit_23, 8, 1, 1, 2)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_3.addWidget(self.lineEdit_20, 7, 1, 1, 2)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_3.addWidget(self.lineEdit_18, 6, 1, 1, 2)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_3.addWidget(self.lineEdit_17, 2, 1, 1, 2)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_3.addWidget(self.lineEdit_14, 3, 1, 1, 2)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_3.addWidget(self.lineEdit_19, 0, 1, 1, 2)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_3.addWidget(self.lineEdit_21, 1, 1, 1, 2)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 12, 0, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_3.addWidget(self.lineEdit_26, 12, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_34)
        self.label_35 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.label_36 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_36)
        self.label_37 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.label_38 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_38)
        self.label_39 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.label_40 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_40)
        self.label_41 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.label_42 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_42)
        self.label_43 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_43)
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def total() :
           t1 = int(self.lineEdit.text())
        #    t2  = int(self.lineEdit.text())
           t3 = int(self.lineEdit_2.text())
           t4 = int(self.lineEdit_3.text())
           t5 = int(self.lineEdit_4.text())
           t6 = int(self.lineEdit_5.text())
           t7 = int(self.lineEdit_6.text())
           t8 = int(self.lineEdit_7.text())
           t9 = int(self.lineEdit_8.text())
           t10 = int(self.lineEdit_9.text())
           t11 = int(self.clothesLineEdit.text())
           t12 = int(self.lineEdit_10.text())
           cost =  t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10 + t11
           estimated = t1 - cost - t12
           daily = estimated/30
           weekly = estimated/4
           self.lineEdit_11.setText(str(cost))
           self.lineEdit_12.setText(str(weekly))
           self.lineEdit_13.setText(str(daily))
           self.lineEdit_19.setText(str(daily))
           return (estimated , cost , daily , weekly)
        self.pushButton_4.clicked.connect(total)
        def daily_total() :
            t1 = int(self.lineEdit_21.text())
            t2 = float(self.lineEdit_19.text())
            t3 = int(self.lineEdit_17.text())
            t4 = int(self.lineEdit_14.text())
            t5 = int(self.lineEdit_15.text())
            t6 = int(self.lineEdit_16.text())
            t7 = int(self.lineEdit_18.text())
            t8 = int(self.lineEdit_23.text())
            t9 = int(self.clothesLineEdit_2.text())
            t10 = int(self.lineEdit_22.text())
            cost =  t1 + t3 + t4 + t5 + t6 + t7 + t8 + t9 
            overbudget = 0
            if cost > t2 :
                overbudget = cost - t2
                self.lineEdit_27.setText(str(overbudget))
            self.lineEdit_24.setText(str(cost))
            date = self.dateEdit.text()
            m = self.lineEdit_26.text()
            self.label_36.setText(str(date))
            self.label_38.setText(str(cost))
            self.label_40.setText(str(t10))
            self.label_42.setText(str(overbudget))
            self.label_43.setText(f"""you were {m} with your expenses""")
        self.pushButton_5.clicked.connect(daily_total)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Daily"))
        self.pushButton_2.setText(_translate("MainWindow", "Weekly"))
        self.pushButton_3.setText(_translate("MainWindow", "Monthly"))
        self.label.setText(_translate("MainWindow", "This application is designed for managing your expenses in diffrent perpotions of time : month , week , day. "))
        self.label_2.setText(_translate("MainWindow", "1- First you can insert you salary and costs in a month and manage the amount of money you spend for each category in a month."))
        self.label_3.setText(_translate("MainWindow", "2- In week section you can make smaller goal for your finance based on the plans you made in month section."))
        self.label_4.setText(_translate("MainWindow", "3- for making sure that you are in right path you can track your expenses daily"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.label_10.setText(_translate("MainWindow", "Education"))
        self.label_5.setText(_translate("MainWindow", "Monthly salary"))
        self.label_12.setText(_translate("MainWindow", "Tax"))
        self.label_9.setText(_translate("MainWindow", "Entertainment"))
        self.label_11.setText(_translate("MainWindow", "Network"))
        self.label_13.setText(_translate("MainWindow", "Accessories"))
        self.label_7.setText(_translate("MainWindow", "Transportation"))
        self.label_8.setText(_translate("MainWindow", "Food"))
        self.label_6.setText(_translate("MainWindow", "Clothes"))
        self.label_14.setText(_translate("MainWindow", "Save"))
        self.clothesLabel.setText(_translate("MainWindow", "Extra"))
        self.label_15.setText(_translate("MainWindow", "Total costs"))
        self.label_16.setText(_translate("MainWindow", "Weekly expense"))
        self.pushButton_4.setText(_translate("MainWindow", "Submit Expenses"))
        self.label_17.setText(_translate("MainWindow", "Daily expense"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Monthly"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "week1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "week2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "week3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "week4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "estimated expense"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "real expense"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "overbudget"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Weekly"))
        self.label_19.setText(_translate("MainWindow", "Education"))
        self.label_20.setText(_translate("MainWindow", "Daily estimated cost"))
        self.label_21.setText(_translate("MainWindow", "Tax"))
        self.label_22.setText(_translate("MainWindow", "Entertainment"))
        self.label_23.setText(_translate("MainWindow", "Network"))
        self.label_24.setText(_translate("MainWindow", "Accessories"))
        self.label_25.setText(_translate("MainWindow", "Transportation"))
        self.label_26.setText(_translate("MainWindow", "Food"))
        self.label_27.setText(_translate("MainWindow", "Clothes"))
        self.label_29.setText(_translate("MainWindow", "Total costs"))
        self.clothesLabel_2.setText(_translate("MainWindow", "Extra"))
        self.label_28.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Submit Expenses"))
        self.label_30.setText(_translate("MainWindow", "Date"))
        self.label_31.setText(_translate("MainWindow", "you can see the results of your one month of tracking your expenses , day by day in next page."))
        self.label_32.setText(_translate("MainWindow", "Satisfaction level"))
        self.label_33.setText(_translate("MainWindow", "Overbudget"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Daily"))
        self.label_34.setText(_translate("MainWindow", "previous day info:"))
        self.label_35.setText(_translate("MainWindow", "Date "))
        self.label_37.setText(_translate("MainWindow", "expenses"))
        self.label_39.setText(_translate("MainWindow", "saved money"))
        self.label_41.setText(_translate("MainWindow", "overbudget amount"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

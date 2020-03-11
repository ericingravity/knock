# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knock_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 290)
        MainWindow.setMinimumSize(QtCore.QSize(372, 290))
        MainWindow.setMaximumSize(QtCore.QSize(372, 290))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("door.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(16, 215, 347, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.reset_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.reset_pushButton.setMinimumSize(QtCore.QSize(50, 24))
        self.reset_pushButton.setMaximumSize(QtCore.QSize(50, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset_pushButton.setFont(font)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.horizontalLayout.addWidget(self.reset_pushButton)
        self.knock_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.knock_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.knock_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.knock_pushButton.setFont(font)
        self.knock_pushButton.setDefault(False)
        self.knock_pushButton.setFlat(False)
        self.knock_pushButton.setObjectName("knock_pushButton")
        self.horizontalLayout.addWidget(self.knock_pushButton)
        self.options_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.options_groupBox.setGeometry(QtCore.QRect(12, 122, 350, 83))
        self.options_groupBox.setMinimumSize(QtCore.QSize(350, 83))
        self.options_groupBox.setMaximumSize(QtCore.QSize(350, 83))
        self.options_groupBox.setObjectName("options_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.options_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.udp_checkBox = QtWidgets.QCheckBox(self.options_groupBox)
        self.udp_checkBox.setMinimumSize(QtCore.QSize(205, 20))
        self.udp_checkBox.setMaximumSize(QtCore.QSize(205, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.udp_checkBox.setFont(font)
        self.udp_checkBox.setToolTip("")
        self.udp_checkBox.setToolTipDuration(-1)
        self.udp_checkBox.setStatusTip("")
        self.udp_checkBox.setObjectName("udp_checkBox")
        self.gridLayout.addWidget(self.udp_checkBox, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(116, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.delay_label = QtWidgets.QLabel(self.options_groupBox)
        self.delay_label.setMinimumSize(QtCore.QSize(74, 22))
        self.delay_label.setMaximumSize(QtCore.QSize(74, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delay_label.setFont(font)
        self.delay_label.setObjectName("delay_label")
        self.horizontalLayout_3.addWidget(self.delay_label)
        self.delay_spinBox = QtWidgets.QSpinBox(self.options_groupBox)
        self.delay_spinBox.setMinimumSize(QtCore.QSize(60, 22))
        self.delay_spinBox.setMaximumSize(QtCore.QSize(60, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delay_spinBox.setFont(font)
        self.delay_spinBox.setMinimum(1)
        self.delay_spinBox.setMaximum(1000)
        self.delay_spinBox.setProperty("value", 200)
        self.delay_spinBox.setObjectName("delay_spinBox")
        self.horizontalLayout_3.addWidget(self.delay_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.annoying_spacer_label = QtWidgets.QLabel(self.options_groupBox)
        self.annoying_spacer_label.setMinimumSize(QtCore.QSize(10, 22))
        self.annoying_spacer_label.setMaximumSize(QtCore.QSize(10, 22))
        self.annoying_spacer_label.setText("")
        self.annoying_spacer_label.setObjectName("annoying_spacer_label")
        self.gridLayout.addWidget(self.annoying_spacer_label, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeout_label = QtWidgets.QLabel(self.options_groupBox)
        self.timeout_label.setMinimumSize(QtCore.QSize(83, 22))
        self.timeout_label.setMaximumSize(QtCore.QSize(83, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeout_label.setFont(font)
        self.timeout_label.setStatusTip("")
        self.timeout_label.setObjectName("timeout_label")
        self.horizontalLayout_2.addWidget(self.timeout_label)
        self.timeout_spinBox = QtWidgets.QSpinBox(self.options_groupBox)
        self.timeout_spinBox.setMinimumSize(QtCore.QSize(60, 22))
        self.timeout_spinBox.setMaximumSize(QtCore.QSize(60, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeout_spinBox.setFont(font)
        self.timeout_spinBox.setMinimum(1)
        self.timeout_spinBox.setMaximum(1000)
        self.timeout_spinBox.setProperty("value", 200)
        self.timeout_spinBox.setObjectName("timeout_spinBox")
        self.horizontalLayout_2.addWidget(self.timeout_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 2, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(12, 10, 354, 112))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.host_label = QtWidgets.QLabel(self.layoutWidget1)
        self.host_label.setMinimumSize(QtCore.QSize(350, 15))
        self.host_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.host_label.setFont(font)
        self.host_label.setObjectName("host_label")
        self.verticalLayout_2.addWidget(self.host_label)
        self.host_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.host_lineEdit.setMinimumSize(QtCore.QSize(350, 15))
        self.host_lineEdit.setMaximumSize(QtCore.QSize(350, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.host_lineEdit.setFont(font)
        self.host_lineEdit.setClearButtonEnabled(True)
        self.host_lineEdit.setObjectName("host_lineEdit")
        self.verticalLayout_2.addWidget(self.host_lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.port_label = QtWidgets.QLabel(self.layoutWidget1)
        self.port_label.setMinimumSize(QtCore.QSize(350, 15))
        self.port_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")
        self.verticalLayout.addWidget(self.port_label)
        self.port_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.port_lineEdit.setMinimumSize(QtCore.QSize(350, 22))
        self.port_lineEdit.setMaximumSize(QtCore.QSize(350, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.port_lineEdit.setFont(font)
        self.port_lineEdit.setClearButtonEnabled(True)
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.verticalLayout.addWidget(self.port_lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStatusTip("")
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setMinimumSize(QtCore.QSize(372, 22))
        self.statusBar.setMaximumSize(QtCore.QSize(372, 22))
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.host_lineEdit, self.port_lineEdit)
        MainWindow.setTabOrder(self.port_lineEdit, self.udp_checkBox)
        MainWindow.setTabOrder(self.udp_checkBox, self.delay_spinBox)
        MainWindow.setTabOrder(self.delay_spinBox, self.timeout_spinBox)
        MainWindow.setTabOrder(self.timeout_spinBox, self.reset_pushButton)
        MainWindow.setTabOrder(self.reset_pushButton, self.knock_pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Knock"))
        self.reset_pushButton.setText(_translate("MainWindow", "Reset"))
        self.knock_pushButton.setText(_translate("MainWindow", "&Knock"))
        self.options_groupBox.setTitle(_translate("MainWindow", " Options "))
        self.udp_checkBox.setText(_translate("MainWindow", "UDP instead of TCP for all ports"))
        self.delay_label.setText(_translate("MainWindow", "Delay (ms):"))
        self.timeout_label.setText(_translate("MainWindow", "Timeout (ms):"))
        self.host_label.setText(_translate("MainWindow", "Hostname or IP address:"))
        self.host_lineEdit.setPlaceholderText(_translate("MainWindow", "192.168.1.100"))
        self.port_label.setText(_translate("MainWindow", "Ports (space seperated):"))
        self.port_lineEdit.setPlaceholderText(_translate("MainWindow", "7000 8000 9000"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLoad.setText(_translate("MainWindow", "Load..."))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

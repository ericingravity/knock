import sys, string, json, os, threading
from knock import Knocker
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from knock_window import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # buttons
        self.knock_pushButton.clicked.connect(self.threaded_knock)
        self.reset_pushButton.clicked.connect(self.reset)

        # menu
        self.actionExit.triggered.connect(self.exit)
        self.actionLoad.triggered.connect(self.load_config)
        self.actionSave_as.triggered.connect(self.save_config)

        # status bar and label (fake status) in the status bar
        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setStyleSheet("QStatusBar::item {border: none;}")
        self.fakeStatus_label = QtWidgets.QLabel()
        self.fakeStatus_label.setText(" Ready")
        self.statusBar.addWidget(self.fakeStatus_label)
        self.setStatusBar(self.statusBar)

        # things that changed
        self.port_lineEdit.textChanged.connect(self.check_text)
        self.host_lineEdit.textChanged.connect(self.generic_something_changed)
        self.udp_checkBox.stateChanged.connect(self.generic_something_changed)
        self.delay_spinBox.textChanged.connect(self.generic_something_changed)
        self.timeout_spinBox.textChanged.connect(self.generic_something_changed)


    # title fix if something changes
    def generic_something_changed(self):
        if self.windowTitle() != "Knock":
            self.setWindowTitle("Knock")


    # enable or disable udp checkbox depending on conditions
    def check_text(self):
        if self.windowTitle() != "Knock":
            self.setWindowTitle("Knock")

        port = self.port_lineEdit.text()
        port = "".join(port.split())
        udp_check = self.udp_checkBox

        if not port:
            udp_check.setEnabled(True)
        elif not port.isnumeric():
            udp_check.setEnabled(False)
        else:
            udp_check.setEnabled(True)


    # load config file
    def load_config(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load", "", "Knock Files (*.knock);;JSON Files (*.json);;All Files (*.*)")

        if filename:
            try:
                with open(filename, 'r') as x:
                    knock = json.load(x)
            except: # indeed
                self.fakeStatus_label.setText(" Error: Unable to load " + os.path.basename(filename))
                return
        else:
            return

        host = knock['host']
        ports = knock['ports']
        udp_state = knock['udp_state']
        if udp_state != 0 and udp_state != 2:
            udp_state = 0
        delay = knock['delay']
        if not str(delay).isnumeric():
            delay = 200
        timeout = knock['timeout']
        if not str(timeout).isnumeric():
            timeout = 200

        self.host_lineEdit.setText(host)
        self.port_lineEdit.setText(ports)
        self.udp_checkBox.setChecked(udp_state)
        self.delay_spinBox.setValue(delay)
        self.timeout_spinBox.setValue(timeout)
        self.setWindowTitle("Knock - [" + os.path.basename(filename) + "]")


    # save config file in json
    def save_config(self):
        knock_dict = {
            "host": self.host_lineEdit.text(),
            "ports": self.port_lineEdit.text(),
            "udp_state": self.udp_checkBox.checkState(),
            "delay": self.delay_spinBox.value(),
            "timeout": self.timeout_spinBox.value()
        }

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save as...", "", "Knock Files (*.knock);;JSON Files (*.json);;All Files (*.*)")
        if filename:
            try:
                with open(filename, 'w') as knock_file:
                    json.dump(knock_dict, knock_file, indent=4)
            except: # welp
                self.fakeStatus_label.setText(" Error: Unable to save " + os.path.basename(filename))
                return
        else:
            return


    # clear fields, reset values
    def reset(self):
        self.host_lineEdit.clear()
        self.port_lineEdit.clear()
        self.delay_spinBox.setValue(200)
        self.timeout_spinBox.setValue(200)
        self.udp_checkBox.setCheckState(False)
        self.setWindowTitle("Knock")
        self.fakeStatus_label.setText(" Ready")


    # perform the knock
    def knock(self):
        # get data from gui
        host = self.host_lineEdit.text()
        ports = self.port_lineEdit.text()
        delay = self.delay_spinBox.text()
        timeout = self.timeout_spinBox.text()
        udp_check = self.udp_checkBox.isChecked()
        udp_enabled = self.udp_checkBox.isEnabled()

        if not host or not ports:
            return

        # arguments to pass to knocker
        args = [
            "-t " + timeout,
            "-d " + delay,
        ]

        if udp_check and udp_enabled:
            args.append("-u")

        args.append(host)

        # add ports to list then add to args[] list
        ports_list = ports.split()

        for i in ports_list:
            args.append(i)

        # send the knock sequence
        try:
            door = Knocker(args)
            door.knock()

            if len(host) > 16:
                self.fakeStatus_label.setText(" Knocked " + host[0:16] + "...")
            else:
                self.fakeStatus_label.setText(" Knocked " + host)

        except: # eek
            self.fakeStatus_label.setText(" Error: Knock failed")


    def threaded_knock(self):
        thread = threading.Thread(target=self.knock, args=())
        thread.start()


    def exit(self):
        exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

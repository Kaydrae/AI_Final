import UIClass
import sys
from PyQt5.QtCore import QTimer

if __name__ == "__main__":
    app = UIClass.QtWidgets.QApplication(sys.argv)
    MainWindow = UIClass.QtWidgets.QMainWindow()
    ui = UIClass.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Timer for clock
    timer = QTimer(MainWindow)
    timer.timeout.connect(ui.clock)
    timer.start(1000)
    MainWindow.show()
    sys.exit(app.exec_())

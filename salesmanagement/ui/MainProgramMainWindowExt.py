import sys
from PyQt6.QtWidgets import QMainWindow
from salesmanagement.ui.MainProgramMainWindow import Ui_MainWindow
from salesmanagement.ui.ProductMainWindowEXT import ProductMainWindowEXT


class MainProgramMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        try:
            self.MainWindow.show()
        except Exception as e:
            print(f"Error showing window: {e}")

    def setupSignalAndSlot(self):
        self.actionthoatphanmem.triggered.connect(self.xuly_thoat)
        self.actionQuanlySanphamDanhMuc.triggered.connect(self.xuly_momanhinh_qlspdm)

    def xuly_thoat(self):
        try:
            sys.exit(0)
        except Exception as e:
            print(f"Error during exit: {e}")

    def xuly_momanhinh_qlspdm(self):
        try:
            self.mainwindow = QMainWindow()
            self.myui = ProductMainWindowEXT()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        except Exception as e:
            print(f"Error during opening product management screen: {e}")

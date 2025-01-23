import traceback

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from salesmanegemant.ibs.nhanvienconnector import NhanVienConnector
from salesmanegemant.ui.LoginMainWindow import Ui_He_Thong_may_Hoc_ABC
from salesmanegemant.ui.MainProgramMainWindowEXT import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_He_Thong_may_Hoc_ABC):
    def __init__(self):
        self.nvconnector = NhanVienConnector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showwindow(self):
        (self.MainWindow.show())
    def setupSignalAndSlot(self):
        self.pushButton_login.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        try:
            username=self.Line_Edit_username.text()
            password=self.Line_edit_Password.text()
            #giả lập đăng nhập (hôm sau truy vấn thật trong CSDL)
            #gọi kết nối cơ sở dữ liệu MySQL
            self.nvconnector.connect()
            self.nvlogin=self.nvconnector.dang_nhap(username,password)
            if self.nvlogin!=None:
                self.MainWindow.hide()
                self.mainwindow = QMainWindow()
                self.myui = MainProgramMainWindowExt()
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()
            else:
                self.msg=QMessageBox()
                self.msg.setWindowTitle("Login thất bại")
                self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
                self.msg.setIcon(QMessageBox.Icon.Critical)
                self.msg.show()
        except:
            traceback.print_exc()
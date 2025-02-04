from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from salesmanagement.libs.nhanvienconnector import NhanVienConnector
from salesmanagement.ui.LoginMainWindow import Ui_MainWindow
from salesmanagement.ui.MainProgramMainWindowExt import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.nvconnector=NhanVienConnector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonDangNhap.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        try:
            username = self.lineEditUserName.text()
            password = self.lineEditPassword.text()

            # Kết nối MySQL và kiểm tra đăng nhập
            self.nvconnector.connect()
            self.nvlogin = self.nvconnector.dang_nhap(username, password)

            if self.nvlogin is not None:
                print("[DEBUG] Chuyển sang màn hình chính...")
                self.MainWindow.hide()

                # Giữ lại tham chiếu tới cửa sổ chính
                self.mainwindow = QMainWindow()
                self.myui = MainProgramMainWindowExt()
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()
            else:
                print("[DEBUG] Đăng nhập thất bại.")
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Login thất bại")
                self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
                self.msg.setIcon(QMessageBox.Icon.Critical)
                self.msg.exec()
        except Exception as e:
            print(f"[ERROR] Lỗi khi đăng nhập: {e}")

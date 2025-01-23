from PyQt6.QtWidgets import QMainWindow, QMessageBox

from salesmanegemant.ui.LoginMainWindow import Ui_He_Thong_may_Hoc_ABC
from salesmanegemant.ui.MainProgramMainWindowEXT import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_He_Thong_may_Hoc_ABC):
    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)
        self.mainWindow = mainWindow
        self.setupSignalAndSlot()
    def showwindow(self):
        (self.mainWindow.show())

    def setupSignalAndSlot(self):
        self.pushButton_login.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        username=self.Line_Edit_username.text()
        password=self.Line_edit_Password.text()
        #giả lập đăng nhập (hôm sau truy vấn thật trong CSDL)
        if username=="admin" and password=="123":
            self.mainWindow.hide()
            self.mainwindow = QMainWindow()
            self.myui = MainProgramMainWindowExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Login thất bại")
            self.msg.setText("Ban dang nhap that bai")
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.show()
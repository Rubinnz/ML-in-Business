import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from salesmanagement.ui.LoginMainWindowExt import LoginMainWindowExt

try:
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    myui = LoginMainWindowExt()
    myui.setupUi(mainwindow)
    myui.showWindow()
    sys.exit(app.exec())
except Exception as e:
    print(f"[ERROR] Lỗi khi chạy chương trình: {e}")

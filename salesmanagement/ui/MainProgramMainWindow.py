# Form implementation generated from reading ui file 'E:\DaiHocKinhTeLuat\2024-2025-HK2\mlkd\K22416C\salesmanagement\ui\MainProgramMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 481)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 140, 521, 61))
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 255, 255);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 22))
        self.menubar.setObjectName("menubar")
        self.menuH_th_ng = QtWidgets.QMenu(parent=self.menubar)
        self.menuH_th_ng.setObjectName("menuH_th_ng")
        self.menuQuanly = QtWidgets.QMenu(parent=self.menubar)
        self.menuQuanly.setObjectName("menuQuanly")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionthongtintaikhoan = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\DaiHocKinhTeLuat\\2024-2025-HK2\\mlkd\\K22416C\\salesmanagement\\ui\\../images/ic_thongtintaikhoan.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionthongtintaikhoan.setIcon(icon)
        self.actionthongtintaikhoan.setObjectName("actionthongtintaikhoan")
        self.actiondoimatkhau = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:\\DaiHocKinhTeLuat\\2024-2025-HK2\\mlkd\\K22416C\\salesmanagement\\ui\\../images/ic_doimatkhau.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actiondoimatkhau.setIcon(icon1)
        self.actiondoimatkhau.setObjectName("actiondoimatkhau")
        self.actioncauhinhhethong = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:\\DaiHocKinhTeLuat\\2024-2025-HK2\\mlkd\\K22416C\\salesmanagement\\ui\\../images/ic_cauhinh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actioncauhinhhethong.setIcon(icon2)
        self.actioncauhinhhethong.setObjectName("actioncauhinhhethong")
        self.actionthoatphanmem = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("E:\\DaiHocKinhTeLuat\\2024-2025-HK2\\mlkd\\K22416C\\salesmanagement\\ui\\../images/ic_exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionthoatphanmem.setIcon(icon3)
        self.actionthoatphanmem.setShortcut("")
        self.actionthoatphanmem.setObjectName("actionthoatphanmem")
        self.actionQuanlySanphamDanhMuc = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("E:\\DaiHocKinhTeLuat\\2024-2025-HK2\\mlkd\\K22416C\\salesmanagement\\ui\\../images/ic_quanly_sanpham.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionQuanlySanphamDanhMuc.setIcon(icon4)
        self.actionQuanlySanphamDanhMuc.setObjectName("actionQuanlySanphamDanhMuc")
        self.actionQuanLyNhanVien = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("E:\\DaiHocKinhTeLuat\\2024-2025-HK2\\mlkd\\K22416C\\salesmanagement\\ui\\../images/ic_quanly_nhanvien.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionQuanLyNhanVien.setIcon(icon5)
        self.actionQuanLyNhanVien.setObjectName("actionQuanLyNhanVien")
        self.actionQuanlyDonHang = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("E:\\DaiHocKinhTeLuat\\2024-2025-HK2\\mlkd\\K22416C\\salesmanagement\\ui\\../images/ic_quanlydonhang.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionQuanlyDonHang.setIcon(icon6)
        self.actionQuanlyDonHang.setObjectName("actionQuanlyDonHang")
        self.menuH_th_ng.addAction(self.actionthongtintaikhoan)
        self.menuH_th_ng.addSeparator()
        self.menuH_th_ng.addAction(self.actiondoimatkhau)
        self.menuH_th_ng.addSeparator()
        self.menuH_th_ng.addAction(self.actioncauhinhhethong)
        self.menuH_th_ng.addSeparator()
        self.menuH_th_ng.addAction(self.actionthoatphanmem)
        self.menuQuanly.addAction(self.actionQuanlySanphamDanhMuc)
        self.menuQuanly.addSeparator()
        self.menuQuanly.addAction(self.actionQuanlyDonHang)
        self.menuQuanly.addSeparator()
        self.menuQuanly.addAction(self.actionQuanLyNhanVien)
        self.menubar.addAction(self.menuH_th_ng.menuAction())
        self.menubar.addAction(self.menuQuanly.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Đây là màn hình chính"))
        self.menuH_th_ng.setTitle(_translate("MainWindow", "Hệ thống"))
        self.menuQuanly.setTitle(_translate("MainWindow", "Quản lý"))
        self.actionthongtintaikhoan.setText(_translate("MainWindow", "Thông tin tài khoản"))
        self.actionthongtintaikhoan.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actiondoimatkhau.setText(_translate("MainWindow", "Đổi mật khẩu"))
        self.actioncauhinhhethong.setText(_translate("MainWindow", "Cấu hình hệ thống"))
        self.actionthoatphanmem.setText(_translate("MainWindow", "Thoát phần mềm"))
        self.actionQuanlySanphamDanhMuc.setText(_translate("MainWindow", "Quản lý sản phẩm - danh mục"))
        self.actionQuanLyNhanVien.setText(_translate("MainWindow", "Quản lý nhân viên"))
        self.actionQuanlyDonHang.setText(_translate("MainWindow", "Quản lý đơn hàng"))

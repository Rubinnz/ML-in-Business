from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem, QMessageBox

from salesmanagement.libs.danhmucconnector import DanhMucConnector
from salesmanagement.libs.sanphamconnector import SanPhamConnector
from salesmanagement.ui.ProductMainWindow import Ui_MainWindow

class ProductMainWindowEXT(Ui_MainWindow):
    def __init__(self):
        self.dmc = DanhMucConnector()
        self.dsdm = []
        self.spc = SanPhamConnector()
        self.dssp = []
        self.current_selected_dm = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.truyvan_danhmucsanpham()
        self.hienthi_danhmucsanpham()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def hienthi_danhmucsanpham(self):
        try:
            self.listWidgetDanhMuc.clear()
            for dm in self.dsdm:
                item = QListWidgetItem()
                item.setData(Qt.ItemDataRole.UserRole, dm)
                item.setText(dm.tendanhmuc)
                self.listWidgetDanhMuc.addItem(item)
        except Exception as e:
            self.show_error_message("Lỗi khi hiển thị danh mục sản phẩm", str(e))

    def truyvan_danhmucsanpham(self):
        try:
            self.dmc.connect()
            self.dsdm = self.dmc.LayToanBoDanhMuc()
            if not self.dsdm:
                raise ValueError("Không có danh mục sản phẩm")
        except Exception as e:
            self.show_error_message("Lỗi khi truy vấn danh mục sản phẩm", str(e))

    def setupSignalAndSlot(self):
        self.listWidgetDanhMuc.itemSelectionChanged.connect(self.tai_danhsach_sanpham)

        self.tableWidgetSanPham.itemSelectionChanged.connect(self.xem_chitiet_sanpham)

        self.pushButtonXoa.clicked.connect(self.xuli_xoa)
    def tai_danhsach_sanpham(self):
        try:
            selected_index = self.listWidgetDanhMuc.currentRow()
            if selected_index < 0:
                return
            item = self.listWidgetDanhMuc.item(selected_index)
            dm = item.data(Qt.ItemDataRole.UserRole)
            self.spc.connect()
            self.dssp = self.spc.LaySanPhamTheoIDDanhmuc(dm.ID)
            self.current_selected_dm = dm

            # Hiển thị sản phẩm trong bảng
            self.hienthi_danhsach_sanpham_len_Qtable()
        except Exception as e:
            self.show_error_message("Lỗi khi tải danh sách sản phẩm", str(e))

    def hienthi_danhsach_sanpham_len_Qtable(self):
        try:
            # Clear the existing rows in the QTableWidget
            self.tableWidgetSanPham.setRowCount(0)

            # Add rows to the table widget
            for p in self.dssp:
                row_index = self.tableWidgetSanPham.rowCount()
                self.tableWidgetSanPham.insertRow(row_index)
                cot_id = QTableWidgetItem(str(p.ID))
                cot_ma =  QTableWidgetItem(p.masanpham)
                cot_ten = QTableWidgetItem(p.tensanpham)
                cot_sl = QTableWidgetItem(str(p.soluong))
                cot_gia = QTableWidgetItem(str(p.dongia))
                cot_iddm = QTableWidgetItem(str(p.IDdanhmuc))
                self.tableWidgetSanPham.setItem(row_index, 0, cot_id)
                self.tableWidgetSanPham.setItem(row_index, 1, cot_ma)
                self.tableWidgetSanPham.setItem(row_index, 2, cot_ten)
                self.tableWidgetSanPham.setItem(row_index, 3, cot_sl)
                self.tableWidgetSanPham.setItem(row_index, 4, cot_gia)
                self.tableWidgetSanPham.setItem(row_index, 5, cot_iddm)
                if p.soluong <=20:
                    cot_sl.setBackground(Qt.GlobalColor.yellow)
                    cot_sl.setForeground(Qt.GlobalColor.red)

        except Exception as e:
            self.show_error_message("Lỗi khi hiển thị sản phẩm", str(e))
    def xem_chitiet_sanpham(self):
        selected_index = self.tableWidgetSanPham.currentRow()
        if selected_index == -1:
            return
        id=self.tableWidgetSanPham.item(selected_index,0).text()
        self.spc.connect()
        sp = self.spc.Lay_chitiet_sanpham(id)
        if sp!=None:
            self.lineEditId.setText(str(sp.ID))
            self.lineEditMa.setText(sp.masanpham)
            self.lineEditTen.setText(sp.tensanpham)
            self.lineEditSoLuong.setText(str(sp.soluong))
            self.lineEditDonGia.setText(str(sp.dongia))
            self.lineEditIdDM.setText(str(sp.IDdanhmuc))

    def xuli_xoa(self):
        msg = self.lineEditId.text()+"-"+self.lineEditTen.text()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác thực xoá")
        dlg.setText("Ê, muốn xoá sản phẩm ["+msg +" hả?")
        dlg.setIcon(QMessageBox.Icon.Question)
        button = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(button)
        result = dlg.exec()
        if result==QMessageBox.StandardButton.No:
            return
        self.spc.connect()
        result=self.spc.xoa_sanpham_theoid(self.lineEditId.text())
        if result>0:
            self.spc.connect()
            self.dssp = self.spc.LaySanPhamTheoIDDanhmuc(self.current_selected_dm.ID)
            self.hienthi_danhsach_sanpham_len_Qtable()



    def show_error_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

from salesmanagement.libs.connector import MySQLConnector
from salesmanagement.models.nhanvien import NhanVien

class NhanVienConnector(MySQLConnector):
    def dang_nhap(self,username,password):
        cursor=self.conn.cursor()
        sql="select * from nhanvien where username=%s and password=%s"
        val = (username,password)
        cursor.execute(sql, val)
        dataset = cursor.fetchone()
        nv=None# giả sử không tìm thấy nhân viên đúng theo USERname +password
        if dataset != None:
            ID, manhanvien, tennhanvien, username, password, isdelete = dataset
            #vào được đây tức là có nhân viên
            nv=NhanVien(ID,manhanvien,tennhanvien,username,password,isdelete)
        cursor.close()
        return nv



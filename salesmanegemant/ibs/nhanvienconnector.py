from salesmanegemant.ibs.conector import MySQLConnector
from salesmanegemant.model.nhanvien import Nhanvien


class NhanVienConnector(MySQLConnector):
    def dang_nhap(self,username, password):
        cursor = self.conn.cursor()
        sql = "select * from nhanvien where username = %s and password = %s"
        val = (username,password)
        cursor.executemany(sql, val)
        dataset = cursor.fetchone()
        nv= None
        if dataset != None:
            ID, code, manhanvien, tennhanvien, username, password , isdelete  =dataset
            nv=Nhanvien(ID, code, manhanvien, tennhanvien, username, password , isdelete)
        cursor.close()
        return nv
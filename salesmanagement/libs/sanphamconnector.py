from salesmanagement.libs.connector import MySQLConnector
from salesmanagement.models.sanpham import SanPham


class SanPhamConnector(MySQLConnector):
    def LaySanPhamTheoIDDanhmuc(self,iddm):
        cursor = self.conn.cursor()
        sql="select * from sanpham where IDdanhmuc=%s"
        val = (iddm,)
        cursor.execute(sql,val)
        dataset = cursor.fetchall()
        dssp=[]
        for item in dataset:
            dssp.append(SanPham(item[0],item[1],item[2],item[3],item[4],item[5]))
        cursor.close()
        return dssp

    def Lay_chitiet_sanpham(self,ID):
        cursor=self.conn.cursor()
        sql="select * from sanpham where ID=%s"
        val = (ID,)
        cursor.execute(sql, val)
        dataset = cursor.fetchone()
        sp=None# giả sử không tìm thấy nhân viên đúng theo USERname +password
        if dataset != None:
            ID, ma, ten, sl, dg, iddm = dataset
            #vào được đây tức là có nhân viên
            sp = SanPham(ID, ma, ten, sl, dg, iddm)
        cursor.close()
        return sp
    def xoa_sanpham_theoid(self,ID):
        cursor=self.conn.cursor()
        sql="delete from sanpham where ID=%s"
        val = (ID,)
        cursor.execute(sql, val)
        self.conn.commit()
        result=cursor.rowcount
        cursor.close()
        return result
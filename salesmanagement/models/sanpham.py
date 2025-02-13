class SanPham:
    def __init__(self,ID, masanpham, tensanpham, soluong, dongia, IDdanhmuc):
        self.ID = ID
        self.masanpham = masanpham
        self.tensanpham = tensanpham
        self.soluong = soluong
        self.dongia = dongia
        self.IDdanhmuc = IDdanhmuc
    def __str__(self):
        msg = f"{self.ID}\t{self.masanpham}\t{self.tensanpham}\t{self.soluong}\t{self.dongia}\t{self.IDdanhmuc}"
        return msg
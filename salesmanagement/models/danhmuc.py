class DanhMuc:
    def __init__(self,ID,madanhmuc,tendanhmuc):
        self.ID=ID
        self.madanhmuc=madanhmuc
        self.tendanhmuc=tendanhmuc
    def __str__(self):
        return f"{self.ID}\t{self.madanhmuc}\t{self.tendanhmuc}"

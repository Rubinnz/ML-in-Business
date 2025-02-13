from pandas.core.computation.common import result_type_many

from salesmanagement.libs import sanphamconnector
from salesmanagement.libs.sanphamconnector import SanPhamConnector

# Khởi tạo đối tượng SanPhamConnector
spc = SanPhamConnector()
spc.connect()

# Lấy danh sách sản phẩm theo danh mục có ID = 1
dssp = spc.LaySanPhamTheoIDDanhmuc(1)
print("Danh sách sản phẩm có danh mục = 1")
for sp in dssp:
    print(sp)

# Kiểm tra chi tiết sản phẩm với ID = 2
ID = 2
spc.connect()
sp = spc.Lay_chitiet_sanpham(ID)  # Truyền tham số ID vào đây

if sp is not None:
    print('*' * 20)
    print(sp)
else:
    print("Không tìm thấy sản phẩm với ID:", ID)

id_remove = 13
spc.connect()
result = spc.xoa_sanpham_theoid(id_remove)
if result > 0:
    print(id_remove, "deleted successfully")
else:
    print("Error: Unable to delete record")
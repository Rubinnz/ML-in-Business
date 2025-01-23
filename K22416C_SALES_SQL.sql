/* Câu 1: Viết lệnh trả về toàn bộ sản phẩm
*/
select * from sanpham
/* Câu 2: Viết lệnh SQL sắp xếp sản phẩm theo đơn giá giảm dần
*/
select * from sanpham order by dongia desc

/* Câu 3: Xuất sản phẩm có cột thành tiên tăng dần và sắp xếp tăng dần
*/
select *, soluong*dongia as thanhtien 
from sanpham
order by thanhtien asc
/* Câu 4:  Viết Sql lấy toàn bộ danh mục*/
select * from danhmuc
/* Câu 5: Lọc ra các sản phẩm thuộc về 1 danh mục bất kì */
select * from sanpham
where IDdanhmuc = 1
/* Câu 6: lọc ra các hoá đơn của 1 khách hàng bất kỳ*/
select * from hoadon 
where IDkhachhang = 2

/* Câu 7: Xuất khách hàng có số hoá đơn nhiều nhất

Câu 8: Xuất khách hàng có trị số hoá đơn cao nhất */

select IDkhachhang, count(*) as SoHoaDon
from hoadon
group by IDkhachhang
order by SoHoaDon desc
limit 1;


select h.IDkhachhang, sum(ct.soluong * ct.dongia) as TongTriSoHoaDon
from hoadon h
join chitiethoadon ct on h.ID = ct.IDhoadon
group by h.IDkhachhang
order by TongTriSoHoaDon desc
limit 1;


/* Câu 9: Viết chức 

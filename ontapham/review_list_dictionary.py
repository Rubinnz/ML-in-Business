dataset=[]
dataset.append({"id":1, "name":"Thuốc trị ghẻ","Price":80})
dataset.append({"id":2, "name":"Thuốc trị hôi nách","Price":100})
dataset.append({"id":3, "name":"Thuốc tăng tự tin","Price":70})

def print_data():
    for product in dataset:
        id = product["id"]
        name = product["name"]
        price = product["Price"]
        infor=f"{id}\t{name}\t{price}"
        print(infor)
#Xuất toàn bộ sản phẩm:
print_data()

#sắp xếp danh sách theo đơn giá tăng dần
def sort_data():
    for i in range (0,len(dataset)):
        for j in range(i+1, len(dataset)):
            pi = dataset[i]
            pj = dataset[j]
            if pi['Price']>pj['Price']:
                dataset[i]=pj
                dataset[j]=pi
sort_data()
print('danh sách sản phẩm sau khi sắp xếp giá tăng dần:')
print_data()

#Hãy viết hàm thêm 1 sản phẩm mới
def add_product():
    id=int(input("nhập mã:"))
    name=input("nhập tên:")
    price=float(input("nhập giá:"))
    product={"id":id,"name":name,"Price":price}
    dataset.append(product)
print("Mời bạn nhập sản phẩm mới:")
add_product()
print("Sau khi nhập mới")
print_data()

dataset[0] = {"id":113,"name":"Thuốc cảm cúm","Price":20}
print("Danh sách sản phẩm sau khi cập nhập:")
print_data()

dataset.pop(1)
print("Danh sách sản phẩm sau khi xoá:")
print_data()
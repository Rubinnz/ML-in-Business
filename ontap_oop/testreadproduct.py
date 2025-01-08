from ontap_oop.filefactory import FileFactory
from ontap_oop.product import Product

ff = FileFactory()
dataset = ff.readData("Mydataset.json",Product)
print("Danh sách sản phẩm:")
for product in dataset:
    print(product)
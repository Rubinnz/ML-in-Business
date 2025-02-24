import os
import pickle
from HousingPricePrediction.coding_pyqt6.housingpricepredictionwindow import Ui_MainWindow


class HousingPricePredictionWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

        # Liệt kê các tệp trong thư mục và thêm vào comboBoxTrainedModel
        self.populate_model_list()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        # Kết nối sự kiện nhấn nút dự đoán
        self.buttonpredict.clicked.connect(self.processpredict)

    def populate_model_list(self):
        # Liệt kê các tệp mô hình trong thư mục
        trainemodelLink = f"C:\\Users\\vuquo\\OneDrive\\Máy tính\\K22416C\\HousingPricePrediction\\trainmodel"
        for filename in os.listdir(trainemodelLink):
            if os.path.isfile(os.path.join(trainemodelLink, filename)) and filename.endswith('.zip'):
                self.comboBoxtrainmodel.addItem(filename)

    def processpredict(self):
        # Lấy giá trị nhập từ giao diện người dùng
        AvgAreaIncome = float(self.lineEditIncome.text())
        AvgAreaHouseAge = float(self.lineEditage.text())
        AvgAreaNumberofRooms = float(self.lineEditroom.text())
        AvgAreaNumberofBedrooms = float(self.lineEditbedroom.text())
        AreaPopulation = float(self.lineEditpopulation.text())

        # Lấy tên mô hình đã chọn
        modelname = ' f"C:\\Users\\vuquo\\OneDrive\\Máy tính\\K22416C\\HousingPricePrediction\\trainmodel\\housingmodel.zip'  # Mô hình mặc định

        # Kiểm tra nếu có lựa chọn mô hình từ comboBox
        if self.comboBoxtrainmodel.currentIndex() != -1:
            modelname = f"../trainmodel/{self.comboBoxtrainmodel.currentText()}"

        try:
            # Tải mô hình từ tệp đã chọn
            with open(modelname, 'rb') as f:
                trainmodel = pickle.load(f)

            # Dự đoán giá trị
            prediction = trainmodel.predict(
                [[AvgAreaIncome, AvgAreaHouseAge, AvgAreaNumberofRooms, AvgAreaNumberofBedrooms, AreaPopulation]])

            # Hiển thị kết quả dự đoán trên giao diện
            print("Kết quả: ", prediction)
            self.lineEditPrice.setText(f"{prediction[0]}")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.lineEditPrice.setText("Lỗi khi tải mô hình!")
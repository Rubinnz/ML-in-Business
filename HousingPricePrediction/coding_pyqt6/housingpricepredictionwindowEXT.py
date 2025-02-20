import os
import pickle
from HousingPricePrediction.coding_pyqt6.housingpricepredictionwindow import Ui_MainWindow

class HousingPricePredictionWindowEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        # Correctly connect the button click to the processpredict function
        self.buttonpredict.clicked.connect(self.processpredict)

    def processpredict(self):
        # Get input values from the user interface
        AVGAreIncome = float(self.lineEditIncome.text())
        AvgAreaHouseAge = float(self.lineEditage.text())
        AvgAreaNumberofRooms = float(self.lineEditroom.text())
        AvgAreaNumberofBedrooms = float(self.lineEditbedroom.text())
        AreaPopulation = float(self.lineEditpopulation.text())

        # Load the trained model
        modelname = '../trainmodel/housingmodel.zip'

        # Load the model
        trainmodel = pickle.load(open(modelname, 'rb'))

        # Make the prediction
        prediction = trainmodel.predict(
            [[AVGAreIncome, AvgAreaHouseAge, AvgAreaNumberofRooms, AvgAreaNumberofBedrooms, AreaPopulation]])

        # Output the result to the UI
        print("Kết quả: ", prediction)
        self.lineEditPrice.setText(f"{prediction[0]}")

    def ModelsList(self):
        # List available models
        model_folder = "./HousingPricePrediction/trainedmodel/"
        models = [f for f in os.listdir(model_folder) if f.endswith('.zip')]
        self.comboBoxtrainmodel.addItems(models)
        self.modelname = self.comboBoxtrainmodel.currentText()

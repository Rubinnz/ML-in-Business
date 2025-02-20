from PyQt6.QtWidgets import QApplication, QMainWindow

from HousingPricePrediction.coding_pyqt6.housingpricepredictionwindowEXT import HousingPricePredictionWindowEXT

app = QApplication([])
mainwindow = QMainWindow()
myui = HousingPricePredictionWindowEXT()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
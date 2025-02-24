import os

trainemodelLink = f"C:\\Users\\vuquo\\OneDrive\\Máy tính\\K22416C\\HousingPricePrediction\\trainmodel"
for filename in os.listdir(trainemodelLink):
    if os.path.isfile(os.path.join(trainemodelLink, filename)) and filename.endswith('.zip'):
        print(filename)


import pickle

with open("C:\d_drive\BTP\CameraCalibration\calibration.pkl", "rb") as file:
    # Load the first object
    data1 = pickle.load(file)
    # And so on...

# Now 'data1' and 'data2' contain the respective objects from the pickle file
print(data1)


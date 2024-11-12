import cv2
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

_model = load_model("C:/Users/HP/OneDrive/Desktop/FP/amritha backend/static/ct_resnet_best_model.hdf5")

def chestScanPrediction(path):
        classes_dir = ["Adenocarcinoma","Large cell carcinoma","Normal","Squamous cell carcinoma"]
        # Loading Image
        img = cv2.imread(path)
        # Normalizing Image
        image = cv2.resize(img,(350,350))
        norm_img = np.array(image)/255
        # Converting Image to Numpy Array
        input_arr_img = np.array([norm_img])
        # Getting Predictions
        pred = np.argmax(_model.predict(input_arr_img))
        # Printing Model Prediction
        return(classes_dir[pred])
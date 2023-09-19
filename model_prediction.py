
import tensorflow as tf
from tensorflow import keras
import numpy as np

class ModelPrediction:
    def __init__(self):
        self.model = keras.models.load_model('models/pitch_prediction_model.h5')

    def predict(self, input_data):
        prediction = self.model.predict(np.array([input_data]))
        return prediction[0]

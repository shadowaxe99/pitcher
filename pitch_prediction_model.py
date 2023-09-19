
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def create_model():
    model = keras.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(10,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))

    model.compile(optimizer='adam', loss='mse', metrics=['mae', 'mse'])

    return model

def train_model(model, train_features, train_labels, epochs):
    history = model.fit(train_features, train_labels, epochs=epochs, validation_split = 0.2)

    return model, history

def evaluate_model(model, test_features, test_labels):
    loss, mae, mse = model.evaluate(test_features, test_labels, verbose=2)

    return loss, mae, mse

def predict(model, new_data):
    prediction = model.predict(new_data)

    return prediction

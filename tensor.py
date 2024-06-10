import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np


# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])  # XOR problem

# Crear el modelo
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=5000, verbose=0)

# Predicción
predictions = model.predict(X)
umbral = 0.3
for i in predictions:
    for j in i:
        if(j<0.3) : 
            print ("0")
        else :
            print("1")

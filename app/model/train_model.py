# app/model/train_model.py
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, Conv2D, MaxPooling2D, Flatten, Concatenate
from tensorflow.keras.models import Model
from app.model.preprocess import preprocess_text_data

def build_multimodal_model(vocab_size=10000, max_len=100, image_shape=(224, 224, 3), num_classes=10):
    # Text branch
    text_input = Input(shape=(max_len,), name="text_input")
    x = Embedding(input_dim=vocab_size, output_dim=128)(text_input)
    x = LSTM(64)(x)
    
    # Image branch
    image_input = Input(shape=image_shape, name="image_input")
    y = Conv2D(32, (3,3), activation="relu")(image_input)
    y = MaxPooling2D((2,2))(y)
    y = Conv2D(64, (3,3), activation="relu")(y)
    y = MaxPooling2D((2,2))(y)
    y = Flatten()(y)
    y = Dense(64, activation="relu")(y)
    
    # Concatenate
    combined = Concatenate()([x, y])
    z = Dense(64, activation="relu")(combined)
    output = Dense(num_classes, activation="softmax", name="diagnosis_output")(z)
    
    model = Model(inputs=[text_input, image_input], outputs=output)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model

if __name__ == "__main__":
    model = build_multimodal_model()
    model.summary()
    # Here you would load your preprocessed text and image data, then train:
    # text_data, tokenizer = preprocess_text_data(loaded_texts)
    # image_data = ... (load and preprocess image files)
    # labels = ... (one-hot encoded labels)
    # model.fit([text_data, image_data], labels, epochs=10, batch_size=32)
    # Save the model
    # model.save("data/trained_models/multimodal_model.h5")

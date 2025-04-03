# app/model/preprocess.py
import os
import json
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from app.config import SCRAPED_DATA_PATH

def preprocess_text_data(text_data, max_words=10000, max_len=100):
    tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
    tokenizer.fit_on_texts(text_data)
    sequences = tokenizer.texts_to_sequences(text_data)
    padded = pad_sequences(sequences, maxlen=max_len, padding="post")
    return padded, tokenizer

def preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    # Normalize to [0,1]
    return img_array / 255.0

def load_scraped_text_data():
    # Example: load and concatenate texts from various JSON files
    text_data = []
    for filename in os.listdir(SCRAPED_DATA_PATH):
        if filename.endswith(".json"):
            with open(os.path.join(SCRAPED_DATA_PATH, filename)) as f:
                data = json.load(f)
                # Extract text fields (this will vary based on the source)
                for item in data if isinstance(data, list) else [data]:
                    if "description" in item:
                        text_data.append(item["description"])
    return text_data

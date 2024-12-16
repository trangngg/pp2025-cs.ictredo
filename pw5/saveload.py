# save_load.py
import pickle
import zlib
import os

def save_data(file_path, data):
    with open(file_path, "wb") as f:
        compressed_data = zlib.compress(pickle.dumps(data))  # Compress and serialize
        f.write(compressed_data)
    print("Data has been saved successfully.")

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            compressed_data = f.read()
            data = pickle.loads(zlib.decompress(compressed_data))  # Decompress and deserialize
        print("Data has been loaded successfully.")
        return data
    else:
        print("No saved data found.")
        return {"students": [], "courses": [], "marks": {}}

import numpy as np
import gzip
import matplotlib.pyplot as plt

def load_data(path):
  with open(path, "rb") as f:   
    return np.frombuffer(gzip.decompress(f.read()), dtype=np.uint8).copy()

X_TRAIN_PATH = "dataset/train-images-idx3-ubyte.gz"
Y_TRAIN_PATH = "dataset/train-labels-idx1-ubyte.gz"

X_TEST_PATH = "dataset/t10k-images-idx3-ubyte.gz"
Y_TEST_PATH = "dataset/t10k-labels-idx1-ubyte.gz"

def main():
  x_train = load_data(X_TRAIN_PATH)[16:].reshape(-1, 28, 28)
  y_train = load_data(Y_TRAIN_PATH)[8:]

if __name__ == "__main__":
  main()

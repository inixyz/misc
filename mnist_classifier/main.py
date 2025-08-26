import numpy as np
import gzip

# X_TRAIN_PATH = "dataset/train-images-idx3-ubyte.gz"
# Y_TRAIN_PATH = "dataset/train-labels-idx1-ubyte.gz"
# 
# X_TEST_PATH = "dataset/t10k-images-idx3-ubyte.gz"
# Y_TEST_PATH = "dataset/t10k-labels-idx1-ubyte.gz"
# 
# def load_data(path):
#   with open(path, "rb") as f:   
#     return np.frombuffer(gzip.decompress(f.read()), dtype=np.uint8).copy()
# 
# 
# def init_weights():
#   fc1 = np.random.rand(784, 128)
#   b1 = np.random.rand(128)
#   fc2 = np.random.rand(128, 10)
#   b2 = np.random.rand(10)
#   return fc1, b1, fc2, b2
# 
# 
# def forward(x, fc1, b1, fc2, b2):
#   x = np.maximum(x @ fc1 + b1, 0) # layer1
#   x = np.maximum(x @ fc2 + b2, 0) # layer2
#   return x
# 
# 
# def backward(loss, fc1, b1, fc2, b2):
#   grad_loss = 1  
#   return grad_fc1, grad_b1, grad_fc2, grad_b2
# 
# 
# def main():
#   x_train = load_data(X_TRAIN_PATH)[16:].reshape(-1, 28, 28)
#   y_train = load_data(Y_TRAIN_PATH)[8:]
# 
#   batch_size = 16 
#   weights = init_weights()
# 
#   x = x_train[:batch_size].reshape(-1, 784)
#   y = np.argmax(forward(x, *weights), axis=1)
# 
#   loss = np.mean((y_train[:batch_size] - y) ** 2)
#   print(loss)

def sum_to_shape(a, shape):
  if a.shape == shape: return a
  a = a.sum(tuple(range(a.ndim - len(shape))))
  axis = tuple(i for i in range(a.ndim) if shape[i] == 1)
  return a.sum(axis).reshape(shape)


class Tensor:
  def __init__(self, data, _prev=()):
    self.data = np.array(data) 
    self.grad = np.zeros_like(self.data)
    self._prev = _prev
    self._grad_fn = lambda: None

  def __repr__(self):
    return f"Tensor(data={self.data}, grad={self.grad})"

  def __add__(self, other):
    if not isinstance(other, Tensor): other = Tensor(other)
    out = Tensor(self.data + other.data, (self, other))

    def add_backward():
      self.grad += sum_to_shape(out.grad, self.grad.shape)
      other.grad += sum_to_shape(out.grad, other.grad.shape)

    out._grad_fn = add_backward 
    return out
  
  def backward(self):
    topo = []
    visited = set()
    def build_topo(v):
      if v not in visited:
        visited.add(v)
        for child in v._prev:
          build_topo(child)
        topo.append(v)
    build_topo(self)

    self.grad = np.ones_like(self.grad)
    for v in reversed(topo):
      v._grad_fn()

def main():
  x = Tensor([2, 3])
  y = Tensor(3)
  z = x + y

  z.backward()

  print("x", x) 
  print("y", y) 
  print("z", z) 

if __name__ == "__main__":
  main()

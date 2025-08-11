class Val:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Val(data={self.data})"

    def __add__(self, other):
        return Val(self.data + other.data)

    def __mul__(self, other):
        return Val(self.data * other.data)

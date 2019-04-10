class Perceptron:

    def __init__(self, size):
        self.weights = [rd.random() for i in range(size)]
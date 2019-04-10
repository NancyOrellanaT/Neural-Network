import random as rd
import numpy as np

x1 = []
x2 = []
t = []

class Perceptron:

    def __init__(self, size):
        self.weights = [rd.random() for i in range(size)]
        self.learning_rate = 0.01

    def calculate_output(self, x):
        weighted_sum = np.dot(x, self.weights)
        return 1 if weighted_sum > 0 else 0

    def train(self, x, t):
        for i in range(len(self.weights)):
            delta_w = self.learning_rate * (t - self.calculate_output(x)) * x[i]
            self.weights[i] = self.weights[i] + delta_w

    def show_weights(self):
        print(self.weights)


def read_input():
    f = open("input.txt", "r") 
    text = f.read()
    lines = text.split("\n")
    
    for line in lines:
        values = line.split(",")
        x1.append(int(values[0]))
        x2.append(int(values[1]))
        t.append(int(values[2]))
        
p = Perceptron(3)
p.show_weights()
read_input()

for a in range(1000):
    for i in range(len(x1)):
        p.train([1, x1[i], x2[i]],t[i])

p.show_weights()

for i in range(len(x1)):
    print(p.calculate_output([1, x1[i], x2[i]]))

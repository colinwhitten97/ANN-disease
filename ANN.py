import numpy as np
import pandas as pd


def sigmoid(x): 
    return 1/(1+np.exp(-x))

def sigmoid_deriv(x):
    return x* (1 - x)


class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],3)
        self.weights2 = np.random.rand(3,1)
        self.y = y
        self.output = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def back_propagation(self):
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_deriv(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_deriv(self.output), self.weights2.T) * sigmoid_deriv(self.layer1)))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

if __name__ == "__main__":
    
    mydf = pd.read_csv('export.csv')
    df_y = mydf.iloc[:,[3]]
    df_x = mydf.iloc[:, [0,1]]
    y_array = df_y.to_numpy()
    x_array = df_x.to_numpy()
    

    X = x_array
    y = y_array
    nn = NeuralNetwork(X,y)
    for i in range(3000):
        nn.feedforward()
        nn.back_propagation()

    print(nn.output)




import torch #imports the PyTorch library,
import torch.nn as nn # imports the nn module from PyTorch, which contains all 
#the tools needed to define and construct neural networks.


class NeuralNet(nn.Module): #This defines a new class called NeuralNet, which is a subclass of nn.Module.
    def __init__(self, input_size, hidden_size, num_classes): #constructor (initializer) of the NeuralNet class
        super(NeuralNet, self).__init__() #calls the constructor of the parent class nn.Module to properly initialize the NeuralNet class.
        self.l1 = nn.Linear(input_size, hidden_size) #line creates a linear layer 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU() #creates an activation function called ReLU (Rectified Linear Unit)
        #most commonly used activation functions in neural networks.
    
    def forward(self, x): #the forward pass is the computation that takes the input data x and produces the output.
        out = self.l1(x) #This line applies the first linear layer to the input x.
        out = self.relu(out) #This line applies the ReLU activation function to the output of the first layer.
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out #This line returns the output of the neural network.

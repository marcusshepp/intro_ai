class Neuron(object):
    
    def __init__(self, set_of_input_weights, set_of_inputs, threshold):
        
        self.threshold = threshold
               
        self.set_of_input_weights = set_of_input_weights
        self.set_of_inputs = set_of_inputs
        self.num_of_inputs = len(self.set_of_inputs)   
        
    def set_threshold(self, value):
        self.threshold = value
    
    def calc_output(self):
        length = self.num_of_inputs
        activation = 0
        output = 0
        for i in range(length):
            activation += self.set_of_input_weights[i] * self.set_of_inputs[i]
            print "Activation: ", activation
        if activation > self.threshold:
            output = 1
        return output

weights = [0.5, 0.1, 0.4]
inputs = [1, 0, 1]
threshold = 0.5
n = Neuron(weights, inputs, 0.5)
print n.calc_output()



from neural_network import *

# example of XOR
train_dataset = [
            [(-0.3,0.0,-1.1,0.4,1.3), [1]],
            [(-0.2,-0.2,-0.3,0.1,2.1), [1]],
            [(-0.4,0.0,-0.7,-0.3,2.2), [1]],
            [(-0.3,-0.2,-0.8,0.1,1.4), [1]]
            ]

nn = NeuralNetwork(learning_rate=0.1, debug=False)
nn.add_layer(n_inputs=5, n_neurons=3)
nn.add_layer(n_inputs=3, n_neurons=1)

nn.train(dataset=train_dataset, n_iterations=100, print_error_report=True)

# test
test_dataset = [
    [(-0.3,0.0,-1.1,0.4,1.3), [1]],
    [(-0.2,-0.2,-0.3,0.1,2.1), [0]]
]
nn.test(test_dataset)

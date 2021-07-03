import pandas as pd
from meb.ball import MEB, MEBwO
import timeit

df = pd.read_csv("src\datasets\mnist\mnist_train.csv", header=None)

def load_number(data, number):
    """
    Loads the MNIST data for a specific number

    Input:
        data (df): MNIST data
        number (int): what number in MNIST to load
    
    Return:
        data_out (numpy.array): MNIST data for specific number
    """
    data = df[df[0] == number]
    data_no_labels = data.drop(labels=0, axis=1)
    data_out = data_no_labels.to_numpy()

    return data_out

def test(data, ball):
    """
    Test accuracy for MEB classifier

    Input:
        data (np.array): testing data
        ball (Ball): fit Ball object
    
    Return:
        acc (float): accuracy of MEB classifier
    """
    n = len(data)
    inside = 0
    for x in data:
        if ball.contains(x):
            inside += 1
    
    acc = 1-inside/n
    return acc

zeros = load_number(data=df, number=0)

print("Fit ball")
start = timeit.default_timer()
ball = MEB().fit(data=zeros, method="socp_heuristic", eps=1e-2)
elapsed = timeit.default_timer() - start

print("Elapsed:\t{}\n".format(elapsed))

numbers = range(1,9+1)

numbers_data = [load_number(data=df, number=i) for i in numbers]

accuracies = [test(data=data, ball=ball) for data in numbers_data]

print(accuracies)
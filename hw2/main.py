import numpy as np

def f(x,y):
    return 5*x*x + 40*x + y*y - 12*y + 127 
    
def partial_d_f(x,y):
    return np.array(10*x + 40, 2*y-12)

def gd(X0, eta, iterations=500): 
    X_prev=X0
    for i in range(iterations):
        X_new=X_prev - eta*partial_d_f(X_prev[0], X_prev[1]) 
        X_prev=X_new
    return X_prev

def calculate(eta, number_of_trails=10): 
    best_X=None
    for trail in range(number_of_trails):
        X0=np.random.uniform(low=-10, high=10, size=(2,)) 
        X=gd(X0, eta)
        if(best_X is None) or (f(X[0], X[1]) < f(best_X[0], best_X[0])):
            best_X=X
            return X

for exp in range(3):
    print(f'experiment:{exp +1}') 
    for eta in [0.1, 0.01, 0.001]:
        X=calculate(eta)
        print(f'\tn: {eta}\n\t\tX: {(X[0], X[1])}\n\t\tf(x,y): {f(X[0], X[1])}')
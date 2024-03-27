from Math import Math
import math
import matplotlib.pyplot as plt



class Gamma_Distribution:
    def __init__(self, alpha, beta):
        if alpha <= 0 or beta <= 0:
            raise ValueError("l and r must be greater than 0")
        self.alpha = alpha
        self.beta = beta
        self.mu = beta/alpha
        self.sigma = math.sqrt(beta)/alpha

    def value_at(self, x):
        if x < 0:
            raise ValueError("x must be greater than 0")
        return (self.alpha**self.beta)*(x**(self.beta-1))*(math.e**(-self.alpha*x))/math.gamma(self.beta)
    
    def prob_less(self, x):
        if x < 0:
            raise ValueError("x must be greater than 0")
        return (1/math.gamma(self.beta)) * Math.lowergamma(self.beta, self.alpha*x)
    
    def prob_greater(self, x):
        if x < 0:
            raise ValueError("x must be greater than 0")
        return 1 - self.prob_less(x)
    
    def graph(self):
        x = range(1, 100)
        y = [self.value_at(i/10) for i in x]
        plt.plot(x,y)
        plt.show()
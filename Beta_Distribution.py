import math
import matplotlib.pyplot as plt
import scipy.special as sp



class Beta_Distribution:
    def __init__(self, alpha, beta):
        # notice that x is only over the range 0-1
        if alpha <= 0:
            raise ValueError("alpha must be greater than 0")
        if beta <= 0:
            raise ValueError("beta must be greater than 0")
        self.alpha = alpha
        self.beta = beta
        self.mu = alpha/(alpha+beta)
        self.sigma = math.sqrt((alpha*beta)/((alpha+beta)**2 * (alpha + beta + 1)))

    def value_at(self, x):
        if x < 0 or x > 1:
            raise ValueError("x must be between 1 and 0 (inclusive)")
        return math.gamma(self.alpha + self.beta)/(math.gamma(self.alpha)*math.gamma(self.beta)) * x**(self.alpha-1) * (1-x)**(self.beta-1)

    def prob_less(self, x):
        if x < 0 or x > 1:
            raise ValueError("x must be between 1 and 0 (inclusive)")
        print(x,sp.betainc(self.alpha, self.beta, x))
        return sp.betainc(self.alpha, self.beta, x)

    def pdf(self, x):
        self.value_at(x)

    def cdf(self, x):
        self.prob_less(x)

    def graph(self, precision = 50):
        x = [i/precision for i in range(0, precision)]
        y = [self.value_at(i) for i in x]
        plt.title("Beta Distribution PDF")
        plt.plot(x,y)
        plt.show()

    def graph_cummulative(self, precision = 50):
        x = [i/precision for i in range(1, precision)]
        y = [self.prob_less(i) for i in x]
        plt.plot(x,y)
        plt.title("Beta Distribution CDF")
        plt.show()
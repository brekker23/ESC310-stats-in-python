import math
import matplotlib.pyplot as plt



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
        if x <= 0 or x >= 1:
            raise ValueError("x must be between 1 and 0 (exclusive)")
        return math.gamma(self.alpha + self.beta)/(math.gamma(self.alpha)*math.gamma(self.beta)) * x**(self.alpha-1) * (1-x)**(self.beta-1)

    def prob_less(self, x):
        if x <= 0 or x >= 1:
            raise ValueError("x must be between 1 and 0 (exclusive)")
        print("lol no single equation for this loser")
        coef = math.gamma(self.alpha + self.beta)/(math.gamma(self.alpha)*math.gamma(self.beta))

    def pdf(self, x):
        self.value_at(x)

    def cdf(self, x):
        self.prob_less(x)
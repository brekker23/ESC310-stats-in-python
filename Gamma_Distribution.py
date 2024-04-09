from Math import Math
import math
import matplotlib.pyplot as plt



class Gamma_Distribution:
    def __init__(self, alpha, beta):
        if alpha <= 0 or beta <= 0:
            raise ValueError("l and r must be greater than 0")
        self.alpha = alpha
        self.beta = beta
        self.theta = 1/beta
        self.mu = beta/alpha
        self.sigma = math.sqrt(beta)/alpha
        self.variance = beta/(alpha**2)
        self.mode = (alpha - 1)/beta if alpha > 1 else 0
        self.skewness = 2/math.sqrt(alpha)

    def value_at(self, x):
        if x < 0:
            raise ValueError("x must be greater than 0")
        return (self.alpha**self.beta)*(x**(self.beta-1))*(math.e**(-self.alpha*x))/math.gamma(self.beta)

    def prob_less(self, x):
        if x < 0:
            raise ValueError("x must be greater than 0")
        return min((1/math.gamma(self.alpha)) * Math.lowergamma(self.alpha, self.beta*x),1)

    def prob_greater(self, x):
        if x < 0:
            raise ValueError("x must be greater than 0")
        return 1 - self.prob_less(x)

    def graph(self, log = False, magnitude = 6, precision = 10):
        x = [i/precision for i in range(1, int(self.mu+magnitude*self.sigma*precision))]
        y = [self.value_at(i) for i in x]
        plt.plot(x,y)
        plt.title("Gamma Distribution PDF")
        if log:
            plt.xscale('log')
        plt.show()

    def graph_cummulative(self, log = False, magnitude = 6, precision = 10):
        x = [i/precision for i in range(1, int(self.mu+magnitude*self.sigma*precision))]
        y = [self.prob_less(i) for i in x]
        plt.plot(x,y)
        plt.title("Gamma Distribution CDF")
        if log:
            plt.xscale('log')
        plt.show()

    def pdf(self, x):
        self.value_at(x)

    def cdf(self, x):
        self.prob_less(x)
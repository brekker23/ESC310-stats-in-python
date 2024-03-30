import math
import matplotlib.pyplot as plt



class Weibull_Distribution:
    def __init__(self, beta, delta):
        self.beta = beta
        self.delta = delta
        self.mu = delta * math.gamma(1 + 1/beta)
        self.sigma = math.sqrt(delta**2 * math.gamma(1 + 2/beta) - delta**2 * math.gamma(1 + 1/beta)**2)

    def value_at(self, x):
        if x <= 0:
            raise ValueError("x must be greater than 0")
        return (self.beta/self.delta) * (x/self.delta)**(self.beta-1) * math.exp(-((x/self.delta)**self.beta))

    def prob_less(self, x):
        return 1 - math.exp(-((x/self.delta)**self.beta))

    def prob_greater(self, x):
        return 1 - self.prob_less(x)

    def graph(self, magnitude = 3, precision = 10):
        x = [i/precision for i in range(1, int((self.mu + 2*self.sigma*magnitude)*precision))]
        y = [self.value_at(i) for i in x]
        plt.plot(x, y)
        plt.show()

    def graph_cummulative(self, log = False, magnitude = 3, precision = 10):
        x = [i/precision for i in range(1, int((self.mu + 2*self.sigma*magnitude)*precision))]
        y = [self.prob_less(i) for i in x]
        plt.plot(x, y)
        if log:
            plt.xscale('log')
        plt.show()

    def pdf(self, x):
        self.value_at(x)

    def cdf(self, x):
        self.prob_less(x)
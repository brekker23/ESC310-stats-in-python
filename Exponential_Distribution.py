import math
from matplotlib import pyplot as plt





class Exponential_Distribution:
    def __init__(self, rate):
        self.rate = rate
        self.mu = 1/rate
        self.variance = 1/(rate**2)

    def pdf(self, x):
        return self.rate * math.exp(-self.rate*x)

    def cdf(self, x):
        return 1 - math.exp(-self.rate*x)

    def graph(self, magnitude = 5, precision = 10):
        x = [i/precision for i in range(0, int(self.rate*magnitude*precision))]
        y = [self.pdf(i) for i in x]
        plt.plot(x, y)
        plt.xlabel("Time")
        plt.ylabel("Probability")
        plt.title("Exponential Distribution")
        plt.show()

    def graph_cummulative(self, magnitude = 5, precision = 10):
        x = [i/precision for i in range(0, int(self.rate*magnitude*precision))]
        y = [self.cdf(i) for i in x]
        plt.plot(x, y)
        plt.xlabel("Time")
        plt.ylabel("Probability")
        plt.title("Cummulative Exponential Distribution")
        plt.show()

    def prob_less(self, x):
        return self.cdf(x)

    def prob_greater(self, x):
        return 1 - self.cdf(x)

    def value_at(self, x):
        return self.pdf(x)
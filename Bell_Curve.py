from Math import Math
import math
from Normal_Distribution import Normal_Distribution
import matplotlib.pyplot as plt


class Bell_Curve:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def prob_less(self, x):
        conversion_factor = (x - self.mu)/self.sigma
        return Normal_Distribution.phi(conversion_factor)

    def prop_greater(self, x):
        return 1 - self.prob_less(x)

    def value_at(self, x):
        conversion_factor = (x - self.mu)/self.sigma
        return Normal_Distribution.value_at(conversion_factor)

    def prob_between(self, x1, x2):
        return self.prob_less(x2) - self.prob_less(x1)

    def graph(self, log = False, magnitude = 5, precision = 10):
        x = [i/precision for i in range(int(self.mu*precision - magnitude*self.sigma*precision), int(self.mu*precision + magnitude*self.sigma*precision))]
        y = [self.value_at(i) for i in x]
        plt.plot(x, y)
        plt.title("Bell Curve PDF")
        if log:
            plt.xscale('log')
        plt.show()

    def graph_cummulative(self, log = False, magnitude = 5, precision = 10):
        x = [i/precision for i in range(int(self.mu*precision - magnitude*self.sigma*precision), int(self.mu*precision + magnitude*self.sigma*precision))]
        y = [self.prob_less(i) for i in x]
        plt.plot(x, y)
        plt.title("Bell Curve CDF")
        if log:
            plt.xscale('log')
        plt.show()

    def pdf(self, x):
        self.value_at(x)

    def cdf(self, x):
        self.prob_less(x)

    def inverse_quantile(self, x):
        return self.mu + self.sigma * Normal_Distribution.inverse_quantile(x)
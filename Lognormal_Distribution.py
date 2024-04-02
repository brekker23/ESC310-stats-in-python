from Math import Math
import math
from Normal_Distribution import Normal_Distribution
import matplotlib.pyplot as plt
import numpy as np


class Lognormal_Distribution:
    def __init__(self, theta, omega):
        self.theta = theta
        self.omega = omega
        self.mu = math.exp(theta + omega**2/2)
        self.sigma = math.exp(2*theta + omega**2) * (math.exp(omega**2) - 1)

    def prob_less(self, x):
        conversion_factor = (Math.ln(x) - self.theta)/self.omega
        return Normal_Distribution.phi(conversion_factor)

    def prop_greater(self, x):
        return 1 - self.prob_less(x)

    def graph(self, log = False, magnitude = 5, precision = 10):
        x = [i/precision for i in range(1, int(self.mu + 2*self.sigma*magnitude*precision))]
        y = [self.value_at(i) for i in x]
        plt.plot(x, y)
        plt.title("Lognormal Distribution PDF")
        if log:
            plt.xscale('log')  # Set the scale of the x axis to 'log'
        plt.show()

    def graph_cummulative(self, log = False, magnitude = 5, precision = 10):
        x = [i/precision for i in range(1, int(self.mu + 2*self.sigma*magnitude*precision))]
        y = [self.prob_less(i) for i in x]
        plt.plot(x, y)
        plt.title("Lognormal Distribution CDF")
        if log:
            plt.xscale('log')
        plt.show()

    def value_at(self, x):
        if x <= 0:
            raise ValueError("x must be greater than 0")
        conversion_factor = (Math.ln(x) - self.theta)/self.omega
        return Normal_Distribution.value_at(conversion_factor)

    def pdf(self, x):
        self.value_at(x)

    def cdf(self, x):
        self.prob_less(x)

    def prob_greater(self, x):
        return 1 - self.prob_less(x)
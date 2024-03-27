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
    
    def graph(self, log = False, magnitude = 5):
        x = np.linspace(max(1, self.mu-2*self.sigma*magnitude), self.mu + 2*self.sigma*magnitude, 400)
        y = [self.value_at(i) for i in x]
        plt.plot(x, y)
        if log:
            plt.xscale('log')  # Set the scale of the x axis to 'log'
        plt.show()

    def value_at(self, x):
        if x <= 0:
            raise ValueError("x must be greater than 0")
        conversion_factor = (Math.ln(x) - self.theta)/self.omega
        return Normal_Distribution.value_at(conversion_factor)
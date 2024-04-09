import math
from matplotlib import pyplot as plt
from Normal_Distribution import Normal_Distribution






class Poisson_Distribution:
    def __init__(self, rate):
        self.rate = rate
        self.mu = rate
        self.variance = rate

    def pmf(self, x):
        return (self.rate**x) * math.exp(-self.rate) / math.factorial(x)

    def cdf(self, x):
        return sum([self.pmf(i) for i in range(x+1)])

    def graph(self, magnitude = 5):
        x = list(range(0, int(self.rate*magnitude)))
        y = [self.pmf(i) for i in x]
        plt.bar(x, y)
        plt.xlabel("Number of Successes")
        plt.ylabel("Probability")
        plt.title("Poisson Distribution")
        plt.show()

    def graph_cummulative(self, magnitude = 5):
        x = list(range(0, int(self.rate*magnitude)))
        y = [self.cdf(i) for i in x]
        plt.bar(x, y)
        plt.xlabel("Number of Successes")
        plt.ylabel("Probability")
        plt.title("Cummulative Poisson Distribution")
        plt.show()

    def normal_approximation(self, x):
        t = (x + 0.5 - self.mu) / math.sqrt(self.variance)
        return Normal_Distribution.phi(t)

    def prob_less(self, x):
        return self.cdf(x)

    def value_at(self, x):
        return self.pmf(x)

    def prob_greater(self, x):
        return 1 - self.cdf(x)
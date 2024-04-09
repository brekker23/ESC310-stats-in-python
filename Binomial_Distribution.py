import matplotlib.pyplot as plt
import scipy.special as sp
import math
from Util import Util
from Normal_Distribution import Normal_Distribution



class Binomial_Distribution:
    def __init__(self, p, n):
        self.p = p
        self.n = n
        self.q = 1 - p
        self.mu = n*p
        self.variance = n*p*(1-p)
        self.sigma = math.sqrt(self.variance)

    def description(self):
        Util.print_file_content("Descriptions/Binomial_Distribution_Description.txt")

    def graph(self):
        x = list(range(0, self.n+1))
        y = [self.pmf(i) for i in x]
        plt.bar(x, y)
        plt.xlabel("Number of Successes")
        plt.ylabel("Probability")
        plt.title("Binomial Distribution")
        plt.show()

    def pmf(self, x):
        return sp.comb(self.n, x) * (self.p**x) * (self.q**(self.n - x))

    def cdf(self, x):
        return sum([self.pmf(i) for i in range(x+1)])

    def __normal_approximation(self, x):
        z = (x-self.n*self.p)/math.sqrt(self.n*self.p*self.q)
        return Normal_Distribution.value_at(z)

    def graph_normal_approximation(self):
        x = list(range(0, self.n+1))
        y = [self.__normal_approximation(i) for i in x]
        plt.plot(x,y)
        plt.xlabel("Number of Successes")
        plt.ylabel("Probability")
        plt.title("Normal Approximation of Binomial Distribution")
        x = list(range(0, self.n+1))
        y = [self.pmf(i) for i in x]
        plt.bar(x, y)
        plt.show()

    def graph_cummulative(self):
        x = list(range(0, self.n+1))
        y = [self.cdf(i) for i in x]
        plt.bar(x, y)
        plt.xlabel("Number of Successes")
        plt.ylabel("Probability")
        plt.title("Cummulative Binomial Distribution")
        plt.show()

    def prob_less(self, x):
        return self.cdf(x)

    def prob_greater(self, x):
        return 1 - self.cdf(x)

    def value_at(self,x):
        return self.pmf(x)
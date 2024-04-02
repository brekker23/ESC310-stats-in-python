from Math import Math
import math
import matplotlib.pyplot as plt

class Normal_Distribution:
    mu = 0
    sigma = 1
    @staticmethod
    def phi(x):
        return Math.erf(x/(math.sqrt(2)))/2 + 0.5

    @staticmethod
    def value_at(x):
        return 1/(math.sqrt(2*math.pi)) * math.exp(-(x**2)/2)

    @staticmethod
    def graph(log = False, precision = 10, magnitude = 5):
        x = [i/precision for i in range(-int(magnitude*precision), int(magnitude*precision))]
        y = [Normal_Distribution.value_at(i) for i in x]
        plt.plot(x, y)
        plt.title("Normal Distribution PDF")
        plt.show()

    @staticmethod
    def prob_less(x):
        return Normal_Distribution.phi(x)

    @staticmethod
    def graph_cummulative(log = False, precision = 10, magnitude = 5):
        x = [i/precision for i in range(-int(magnitude*precision), int(magnitude*precision))]
        y = [Normal_Distribution.phi(i) for i in x]
        plt.plot(x, y)
        plt.title("Normal Distribution CDF")
        if log:
            plt.xscale('log')
        plt.show()

    @staticmethod
    def pdf(x):
        Normal_Distribution.value_at(x)

    @staticmethod
    def cdf(x):
        Normal_Distribution.prob_less(x)
from Math import Math
import math
import matplotlib.pyplot as plt
import scipy.special as sp
from Util import Util

class Normal_Distribution:
    mu = 0
    sigma = 1
    @staticmethod
    def phi(x):
        return Math.erf(x/(math.sqrt(2)))/2 + 0.5

    @staticmethod
    def description():
        Util.print_file_content("Descriptions/Normal_Distribution_Description.txt")


    @staticmethod
    def value_at(x):
        return 1/(math.sqrt(2*math.pi)) * math.exp(-(x**2)/2)

    @staticmethod
    def graph(log = False, precision = 10, magnitude = 5):
        x = [i/precision for i in range(-int(magnitude*precision), int(magnitude*precision))]
        y = [Normal_Distribution.value_at(i) for i in x]
        plt.plot(x, y)
        plt.xlabel("X value")
        plt.ylabel("Probability")
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
        plt.xlabel("X value")
        plt.ylabel("Probability")
        if log:
            plt.xscale('log')
        plt.show()

    @staticmethod
    def pdf(x):
        Normal_Distribution.value_at(x)

    @staticmethod
    def cdf(x):
        Normal_Distribution.prob_less(x)

    @staticmethod
    def sample_x_bar(data):
        return sum(data)/len(data)

    @staticmethod
    def sample_variance(data):
        x_bar = Normal_Distribution.sample_x_bar(data)
        return sum([(x - x_bar)**2 for x in data])/(len(data)-1)

    @staticmethod
    def sample_std_dev(data):
        return math.sqrt(Normal_Distribution.sample_variance(data))

    @staticmethod
    def inverse_quantile(x):
        if x < 0 or x > 1:
            raise ValueError("x must be between 0 and 1 (inclusive)")
        ans = math.sqrt(2)*sp.erfinv(2*x-1)
        return ans

    @staticmethod
    def prob_greater(x):
        return 1 - Normal_Distribution.phi(x)

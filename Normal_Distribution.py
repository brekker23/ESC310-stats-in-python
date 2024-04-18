from Math import Math
import math
import matplotlib.pyplot as plt
import scipy.special as sp
from Util import Util

class Normal_Distribution:
    """
    A class representing the Normal Distribution.

    Attributes:
    - mu: The mean of the normal distribution (default: 0).
    - sigma: The standard deviation of the normal distribution (default: 1).
    """

    mu = 0
    sigma = 1

    @staticmethod
    def phi(x):
        """
        Calculate the probability density function (PDF) of the standard normal distribution.

        Args:
        - x: The value at which to calculate the PDF.

        Returns:
        The PDF value at the given x.
        """
        return Math.erf(x/(math.sqrt(2)))/2 + 0.5

    @staticmethod
    def description():
        """
        Print the description of the Normal Distribution from the file "Descriptions/Normal_Distribution_Description.txt".
        """
        Util.print_file_content("Descriptions/Normal_Distribution_Description.txt")

    @staticmethod
    def value_at(x):
        """
        Calculate the probability density function (PDF) of the normal distribution.

        Args:
        - x: The value at which to calculate the PDF.

        Returns:
        The PDF value at the given x.
        """
        return 1/(math.sqrt(2*math.pi)) * math.exp(-(x**2)/2)

    @staticmethod
    def graph(log=False, precision=10, magnitude=5):
        """
        Plot the probability density function (PDF) of the normal distribution.

        Args:
        - log: Whether to use a logarithmic scale for the x-axis (default: False).
        - precision: The precision of the x-axis values (default: 10).
        - magnitude: The magnitude of the x-axis range (default: 5).
        """
        x = [i/precision for i in range(-int(magnitude*precision), int(magnitude*precision))]
        y = [Normal_Distribution.value_at(i) for i in x]
        plt.plot(x, y)
        plt.xlabel("X value")
        plt.ylabel("Probability")
        plt.title("Normal Distribution PDF")
        plt.show()

    @staticmethod
    def prob_less(x):
        """
        Calculate the cumulative distribution function (CDF) of the normal distribution.

        Args:
        - x: The value at which to calculate the CDF.

        Returns:
        The CDF value at the given x.
        """
        return Normal_Distribution.phi(x)

    @staticmethod
    def graph_cummulative(log=False, precision=10, magnitude=5):
        """
        Plot the cumulative distribution function (CDF) of the normal distribution.

        Args:
        - log: Whether to use a logarithmic scale for the x-axis (default: False).
        - precision: The precision of the x-axis values (default: 10).
        - magnitude: The magnitude of the x-axis range (default: 5).
        """
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
        """
        Calculate the probability density function (PDF) of the normal distribution.

        Args:
        - x: The value at which to calculate the PDF.

        Returns:
        The PDF value at the given x.
        """
        Normal_Distribution.value_at(x)

    @staticmethod
    def cdf(x):
        """
        Calculate the cumulative distribution function (CDF) of the normal distribution.

        Args:
        - x: The value at which to calculate the CDF.

        Returns:
        The CDF value at the given x.
        """
        Normal_Distribution.phi(x)

    @staticmethod
    def sample_x_bar(data):
        """
        Calculate the sample mean (x-bar) of a given data set.

        Args:
        - data: The data set.

        Returns:
        The sample mean (x-bar).
        """
        return sum(data)/len(data)

    @staticmethod
    def sample_variance(data):
        """
        Calculate the sample variance of a given data set.

        Args:
        - data: The data set.

        Returns:
        The sample variance.
        """
        x_bar = Normal_Distribution.sample_x_bar(data)
        return sum([(x - x_bar)**2 for x in data])/(len(data)-1)

    @staticmethod
    def sample_std_dev(data):
        """
        Calculate the sample standard deviation of a given data set.

        Args:
        - data: The data set.

        Returns:
        The sample standard deviation.
        """
        return math.sqrt(Normal_Distribution.sample_variance(data))

    @staticmethod
    def inverse_quantile(x):
        """
        Calculate the inverse quantile (quantile function) of the normal distribution.

        Args:
        - x: The quantile value (between 0 and 1).

        Returns:
        The value corresponding to the given quantile.
        """
        if x < 0 or x > 1:
            raise ValueError("x must be between 0 and 1 (inclusive)")
        ans = math.sqrt(2)*sp.erfinv(2*x-1)
        return ans

    @staticmethod
    def z_at_alpha(alpha):
        dict = {0.05: 1.64, 0.1: 1.28, 0.025: 1.96, 0.01: 2.33, 0.005: 2.58}
        if alpha in dict:
            return dict[alpha]
        else:
            raise NotImplementedError("implement z_at_alpha in Normal_Distribution")

    @staticmethod
    def prob_greater(x):
        """
        Calculate the probability of a value being greater than x in the normal distribution.

        Args:
        - x: The value.

        Returns:
        The probability of a value being greater than x.
        """
        return 1 - Normal_Distribution.phi(x)

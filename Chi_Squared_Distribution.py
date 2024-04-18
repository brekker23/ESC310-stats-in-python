import math
import scipy as sp






class Chi_Squared_Distribution:
    def __init__(self, degrees_of_freedom):
        self.k = degrees_of_freedom

    def cdf(self, x):
        if x < 0:
            raise ValueError("x must be greater than or equal to 0")
        coef = 1/math.gamma(self.k/2)
        return coef * sp.special.gammainc(self.k/2, x/2)

    def pdf(self, x):
        if x < 0:
            raise ValueError("x must be greater than or equal to 0")
        coef = 1/(2**(self.k/2) * math.gamma(self.k/2))
        return coef * x**(self.k/2 - 1) * math.exp(-x/2)

    def prob_less(self, x):
        return self.cdf(x)

    def prob_greater(self, x):
        return 1-self.cdf(x)

    def value_at(self, x):
        return self.pdf(x)

    def get_x(self, alpha):


if __name__ == "__main__":
    # Create a test Chi-Squared object with 5 degrees of freedom
    chi_squared = Chi_Squared_Distribution(3)

    # Find the CDF of the Chi-Squared distribution at various points
    points = [1, 2, 3, 4, 5]
    for point in points:
        cdf_value = chi_squared.cdf(point)
        print(f"CDF at point {point}: {cdf_value}")
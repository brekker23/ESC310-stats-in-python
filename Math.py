import math
import matplotlib.pyplot as plt
import scipy as sp

class Math:
    @staticmethod
    def find_closest_value(func, target, initial_guess = 1, tolerance = 0.05, range = [-1000, 1000]):
        guess = initial_guess
        value = func(guess)
        min_guess_error = 4



    @staticmethod
    def get_factorials_below(upto, include_zero = False):
        f = [1] if include_zero else []
        start = 1
        value = 1
        for i in range(start,upto+1):
            value *= i
            f.append(value)
        return f

    @staticmethod
    def ln(x):
        return math.log(x)/math.log(math.e)

    @staticmethod
    def log2(x):
        return math.log(x)/math.log(2)

    @staticmethod
    def lowergamma(s, x):
        return sp.special.gammainc(s, x)

    @staticmethod
    def integrate(f, a, b, n, method = "midpoint"):
        if method == "midpoint":
            return Math.__midpoint(f, a, b, n)
        if method == "trapezoid":
            return Math.__trapezoid(f, a, b, n)
        if method == "simpsons":
            return Math.__simpsons(f, a, b, n)
        raise ValueError("method must be midpoint, trapezoid, or simpsons")

    @staticmethod
    def __midpoint(f, a, b, n=1000):
        w = (b-a)/n
        sum = 0
        for i in range(0,n):
            sum += f(a + w*(i + 0.5))
        return w*sum

    @staticmethod
    def __trapezoid(f, a, b, n=1000):
        w = (b-a)/n
        sum = 0
        for i in range(0,n):
            sum += w*(f(a + w*i) + f(a + w*(i+1)))/2
        return sum

    @staticmethod
    def __simpsons(f, a, b, n=1000):
        w = (b-a)/n
        sum = 0
        for i in range(0,n):
            sum += w*(f(a + w*i) + 4*f(a + w*(i + 0.5)) + f(a + w*(i+1)))/6
        return sum

import math
import matplotlib.pyplot as plt

class Math:
    @staticmethod
    def erf(x):
        if x > 3:
            return 1
        if x < -3:
            return -1
        depth = math.ceil(max(20, 10*abs(x**2)))
        f = Math.__get_factorials_below(depth, include_zero = True)
        coef = 2/(math.sqrt(math.pi))
        terms = []
        for i in range(0,depth):
            term = ((-1)**i) * (x**(2*i + 1)) / (f[i]*(2*i + 1))
            terms.append(term)
        return coef * sum(terms)


    @staticmethod
    def __get_factorials_below(upto, include_zero = False):
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
    def lowergamma(s, x, depth = 20):
        if x < 0 or s < 0:
            raise ValueError("x and s must be greater than 0")
        coef = (x**s)*math.gamma(s)*math.e**(-x)
        terms = []
        for i in range(0, depth):
            term = (x**i)/math.gamma(s+i+1)
            terms.append(term)
        return coef * sum(terms)

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
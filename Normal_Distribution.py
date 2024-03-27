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
    def graph():
        x = [i/100 for i in range(-500, 500)]
        y = [Normal_Distribution.value_at(i) for i in x]
        plt.plot(x, y)
        plt.show()
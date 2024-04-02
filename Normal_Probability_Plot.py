from Normal_Distribution import Normal_Distribution
import matplotlib.pyplot as plt
import scipy.special as sp
from Bell_Curve import Bell_Curve



class Normal_Probability_Plot:
    def __init__(self, data):
        if len(data) < 10:
            print("Warning: The sample size is less than 10. The results may not be accurate.")
        self.sample_x_bar = sum(data)/len(data)
        self.sample_s = Normal_Distribution.sample_std_dev(data)
        self.bell_curve = Bell_Curve(self.sample_x_bar, self.sample_s)
        self.data = data

    def plot(self):
        data = sorted(self.data)
        y = []
        if len(data) < 10:
            a = 3/8
        else:
            a = 0.5
        for i in range(len(data)):
            i+=1
            p = self.bell_curve.inverse_quantile((i - a)/(len(data) - 2*a + 1))
            y.append(p)
        plt.scatter(data, y)
        y = [(0 - data[0])*-1,(data[-1] - 0)]
        x = [data[0], data[-1]]
        plt.plot(x, y, color='red')
        plt.xlabel("Actual Quantiles")
        plt.ylabel("Theoretical Quantiles")
        plt.title("Normal Probability Plot")
        plt.show()
from Normal_Probability_Plot import Normal_Probability_Plot
from Normal_Distribution import Normal_Distribution




class Dataset:
    def __init__(self, data):
        self.data = data
        self.s = self.find_s()
        self.x_bar = self.find_x_bar()

    def add_data(self, new_data):
        self.data.extend(new_data)

    def remove_data(self, data):
        for i in data:
            self.data.remove(i)

    def normal_probability_plot(self):
        npp = Normal_Probability_Plot(self.data)
        npp.plot()

    def find_x_bar(self):
        return sum(self.data)/len(self.data)

    def find_s(self):
        return Normal_Distribution.sample_std_dev(self.data)
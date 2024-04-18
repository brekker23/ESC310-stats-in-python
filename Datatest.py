from Dataset import Dataset
from Util import Util
import math


class Datatest:
    @staticmethod
    def fit_data_to_distribution(data):
        if not isinstance(data, Dataset):
            try:
                data = Dataset(data)
            except:
                raise ValueError("data must be a Dataset object or a list of values")

        # Find the distribution that best fits the data

    @staticmethod
    def compare_data(data1, data2):
        data1 = Util.dataset(data1)
        data2 = Util.dataset(data2)
        if not (data1.distribution != 'unknown' and data2.distribution != 'unknown' and data1.distribution == data2.distribution):
            raise ValueError("data1 and data2 must have the same distributions")

        # Compare the data

    @staticmethod
    def linear_function_of_independant_data(data, weight):
        if len(data) != len(weight):
            raise ValueError("data and weight must be the same length")
        x_bar = 0
        v = 0
        for i in range(len(data)):
            if not isinstance(data[i], Dataset):
                try:
                    data[i] = Dataset(data[i])
                except:
                    raise ValueError("data must be a Dataset object or a list of values")
            if not isinstance(weight[i], (int, float)):
                raise ValueError("weight must be a scalar")
            x_bar += data[i].x_bar * weight[i]
            v += data[i].s**2 * weight[i]**2
        return Dataset(x_bar, math.sqrt(v))

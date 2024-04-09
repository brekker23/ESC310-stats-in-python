from Dataset import Dataset
from Util import Util



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
    def linear_functions_of_independant_data(data1, data2, weight1 = 1, weight2 = 1):
        data1 = Util.dataset(data1)
        data2 = Util.dataset(data2)

        data1*weight1 + data2*weight2
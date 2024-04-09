from Dataset import Dataset





class Util:
    @staticmethod
    def print_file_content(file_path):
        with open(file_path, 'r') as file:
            print(file.read())

    @staticmethod
    def dataset(data):
        if isinstance(data, Dataset):
            return data
        return Dataset(data)

    @staticmethod
    def prob_series(probabilities):
        p = 1
        for prob in probabilities:
            if prob < 0 or prob > 1:
                raise ValueError("probabilities must be between 0 and 1")
            p *= prob
        return p

    @staticmethod
    def prob_parallel(probabilities):
        p = 1
        for prob in probabilities:
            if prob < 0 or prob > 1:
                raise ValueError("probabilities must be between 0 and 1")
            p *= (1-prob)
        return p
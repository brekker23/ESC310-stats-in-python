




class Dataset:
    def __init__(self, data):
        if isinstance(data, Dataset):
            self.data = data.data
        self.data = data
        self.s = self.find_s()
        self.x_bar = self.find_x_bar()
        self.distribution = "unknown"

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __add__(self, other):
        if len(other) == len(self):
            return Dataset([self.data[i] + other.data[i] for i in range(len(self))])
        raise ValueError("Datasets must be the same length to add them")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Dataset([i*other for i in self.data])
        elif isinstance(other, Dataset):
            if len(other) == len(self):
                return sum([self.data[i]*other.data[i] for i in range(len(self))])
            raise ValueError("Datasets must be the same length to multiply them")
        raise ValueError("Dataset can only be multiplied by a scalar or another dataset")

    def __sub__(self, other):
        if len(other) == len(self):
            return Dataset([self.data[i] - other.data[i] for i in range(len(self))])
        raise ValueError("Datasets must be the same length to subtract them")

    def __div__(self, other):
        if isinstance(other, (int, float)):
            return Dataset([i/other for i in self.data])
        elif isinstance(other, Dataset):
            if len(other) == len(self):
                return Dataset([self.data[i]/other.data[i] for i in range(len(self))])
            raise ValueError("Datasets must be the same length to divide them")
        raise ValueError("Dataset can only be divided by a scalar or another dataset")

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __repr__(self):
        return str(self.data), self.x_bar

    def add_data(self, new_data):
        self.data.extend(new_data)

    def remove_data(self, data):
        for i in data:
            self.data.remove(i)

    def find_x_bar(self):
        return sum(self.data)/len(self.data)

    def find_s(self):
        return (sum([(i - self.x_bar)**2 for i in self.data])/len(self.data))**0.5
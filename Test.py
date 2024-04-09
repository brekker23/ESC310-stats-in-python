from Math import Math
import matplotlib.pyplot as plt
import numpy as np
import math
from Normal_Distribution import Normal_Distribution
from Bell_Curve import Bell_Curve
from Lognormal_Distribution import Lognormal_Distribution
from Gamma_Distribution import Gamma_Distribution
from Weibull_Distribution import Weibull_Distribution
from Beta_Distribution import Beta_Distribution
from Normal_Probability_Plot import Normal_Probability_Plot
from Dataset import Dataset
from Binomial_Distribution import Binomial_Distribution
from Poisson_Distribution import Poisson_Distribution
from Exponential_Distribution import Exponential_Distribution

data = np.random.normal(loc=5, scale=10, size=100).tolist()
# n = Normal_Distribution()
# n.graph()
# n.graph_cummulative(magnitude = 5, precision = 20)

# b = Bell_Curve(50, 2.5)
# b.graph()
# b.graph_cummulative(magnitude=5, precision=20)

# l = Lognormal_Distribution(1, .4)
# l.graph()
# l.graph_cummulative(magnitude=5, precision=20)

# g = Gamma_Distribution(3, 5)
# g.graph()
# g.graph_cummulative(magnitude = 5, precision=20)

# w = Weibull_Distribution(2, 5)
# w.graph()
# w.graph_cummulative(magnitude=5, precision=20)

# b = Beta_Distribution(2, 5)
# b.graph()
# b.graph_cummulative(precision=20)


# npp = Normal_Probability_Plot(data)
# npp.plot()

# d = Dataset(data)
# d.normal_probability_plot()

# b = Binomial_Distribution(.4, 10)
# b.graph()
# b.graph_cummulative()

# p = Poisson_Distribution(11.5)
# p.graph()
# p.graph_cummulative()

# e = Exponential_Distribution(2)
# e.graph()
# e.graph_cummulative()

b = Binomial_Distribution(.4, 10)
b.graph_normal_approximation()
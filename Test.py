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

b = Beta_Distribution(2, 5)
b.graph()
b.graph_cummulative(precision=20)

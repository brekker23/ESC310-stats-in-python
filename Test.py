from Math import Math
import matplotlib.pyplot as plt
import numpy as np
import math
from Normal_Distribution import Normal_Distribution
from Bell_Curve import Bell_Curve
from Lognormal_Distribution import Lognormal_Distribution
from Gamma_Distribution import Gamma_Distribution

# n = Normal_Distribution()
# print(n.phi(1))
# n.graph()

# b = Bell_Curve(50, 2.5)
# print(b.prob_less(55))
# b.graph()

# l = Lognormal_Distribution(1, .4)
# print(l.prob_less(55))
# print(l.mu)
# print(l.sigma)
# l.graph()

g = Gamma_Distribution(3, 5)
print(g.prob_less(2))
print(g.value_at(2))
g.graph()
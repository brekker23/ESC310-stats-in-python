from Dataset import Dataset
from Util import Util
import math
from Normal_Distribution import Normal_Distribution
from Math import Math




class Hypothesis_Testing:
    def __init__(self, *data):
        if len(data) > 1:
            print("fix handling multiple datasets")
            raise ValueError("Can only handle one dataset at a time")
        self.data = Util.dataset(data[0])
        self.n = len(self.data)
        self.degrees_of_freedom = self.n - 1

    def p_value_of_mu_variance_known(self, sigma, hypothesis, side = 'middle', distribution = 'normal'):
        if side not in ['left', 'right', 'middle']:
            raise ValueError("side must be 'left', 'right', or 'middle'")
        sample_deviation = sigma/len(self.data)
        sample_mean = self.data.x_bar
        if distribution == 'normal':
            z = (sample_mean - hypothesis)/(sample_deviation)
            if side == 'middle':
                p = 2*(1 - Normal_Distribution.phi(abs(z)))
            elif side == 'left':
                p = 1 - Normal_Distribution.phi(abs(z))
            else:
                p = Normal_Distribution.phi(abs(z))
            return p
        elif distribution == 'lognormal':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'exponential':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'uniform':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'binomial':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'poisson':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'beta':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'gamma':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'weibull':
            raise ValueError("Distribution not yet supported")
        else:
            raise ValueError("Distribution not recognized")

    def z_test_of_mu_variance_known(self, sigma, hypothesis, alpha = 0.05, side = 'middle', distribution = 'normal'):
        p = self.p_value_of_mu_variance_known(sigma, hypothesis, side, distribution)
        if p > alpha:
            return True
        return False

    def confidence_interval_on_mu_variance_known(self, sigma, alpha = 0.05, side = 'middle', distribution = 'normal'):
        sample_deviation = sigma/len(self.data)
        sample_mean = self.data.x_bar

        if distribution == 'normal':
            if side == 'middle':
                z = Normal_Distribution.z_at_alpha(alpha/2)
                lower_bound = sample_mean - z*sample_deviation
                upper_bound = sample_mean + z*sample_deviation
                return lower_bound, upper_bound
            elif side == 'left':
                z = Normal_Distribution.z_at_alpha(alpha)
                upper_bound = sample_mean + z*sample_deviation
                return -math.inf, upper_bound
            else:
                z = Normal_Distribution.z_at_alpha(alpha)
                lower_bound = sample_mean - z*sample_deviation
                return lower_bound, math.inf

        elif distribution == 'lognormal':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'exponential':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'uniform':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'binomial':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'poisson':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'beta':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'gamma':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'weibull':
            raise ValueError("Distribution not yet supported")
        else:
            raise ValueError("Distribution not recognized")

    def reccomended_sample_size(self, sigma, E, alpha = 0.05, distribution = 'normal'):
        n = math.ceil((Normal_Distribution.z_at_alpha(alpha/2)*sigma/E)**2)
        return n

    def p_value_of_mu_variance_unknown(self, hypothesis, side = 'middle', distribution = 'normal'):
        if side not in ['left', 'right', 'middle']:
            raise ValueError("side must be 'left', 'right', or 'middle'")
        sample_deviation = self.data.sample_std_dev
        sample_mean = self.data.x_bar
        t = (sample_mean - hypothesis)/(sample_deviation/math.sqrt(self.n))
        if distribution == 'normal':
            if side == 'middle':
                p = 2*(1 - Normal_Distribution.phi(abs(t)))
            elif side == 'left':
                p = 1 - Normal_Distribution.phi(abs(t))
            else:
                p = Normal_Distribution.phi(abs(t))
            return p
        elif distribution == 'lognormal':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'exponential':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'uniform':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'binomial':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'poisson':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'beta':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'gamma':
            raise ValueError("Distribution not yet supported")
        elif distribution == 'weibull':
            raise ValueError("Distribution not yet supported")
        else:
            raise ValueError("Distribution not recognized")

    def __calculate_t_pdf(self, x):
        return (math.gamma((self.degrees_of_freedom + 1)/2)/(math.sqrt(math.pi*self.degrees_of_freedom)*math.gamma(self.degrees_of_freedom/2)))*(1/((1 + x**2/self.degrees_of_freedom)**((self.degrees_of_freedom + 1)/2)))

    def approximate_t_cdf(self, x, n):
        if n > 30:
            return Normal_Distribution.phi(x)
        else:
            return Math.integrate(self.__calculate_t_pdf, -1000, x, n*1000, method = 'simpsons')

    def chi_squared_test(self, hypothesis, alpha = 0.05, side = 'middle'):
        chi0_squared = ((self.data.s)**2)*(self.n - 1)/(hypothesis**2)
        u =

if __name__ == "__main__":
    # Create a test dataset
    hypothesis_test = Hypothesis_Testing(Dataset([1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5, 7, 5, 5, 5, 5, 10]))

    # Perform hypothesis testing
    sigma = 3
    hypothesis = 4.9
    p_value = hypothesis_test.p_value_of_mu_variance_known(sigma, hypothesis, side = "middle")
    conf_int = hypothesis_test.confidence_interval_on_mu_variance_known(sigma, alpha=0.05)
    sam = hypothesis_test.reccomended_sample_size(sigma, 3, alpha=0.01)
    accept = hypothesis_test.z_test_of_mu_variance_known(sigma, hypothesis, alpha=0.05, side = 'middle')
    t_val = hypothesis_test.approximate_t_cdf(2.57, 10)

    # Print the p-value
    print("P-value:", p_value)
    print("Accept Null Hypothesis:", accept)
    print("Confidence Interval:", conf_int)
    print("Recommended Sample Size:", sam)
    print("T Value:", t_val)
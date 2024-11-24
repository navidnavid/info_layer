import numpy as np
import scipy.stats as stats
import math

#  signal = np.array([[5, 6], [7, 8]])
class info:
    def calculate_entropy(self, signal, num_bins):
        """
        Calculates the Shannon entropy of a 3D signal.

        Args:
            signal: A 3D NumPy array representing the signal.
            num_bins: The number of bins for discretization.

        Returns:
            The Shannon entropy of the signal.
        """

        # Flatten the 3D signal into a 1D array
        signal_flattened = signal.flatten()

        # Discretize the signal using fixed-width bins
        hist, bin_edges = np.histogram(signal_flattened, bins=num_bins, density=True)

        # Calculate the probability distribution
        prob_dist = hist / np.sum(hist)

        # Calculate the entropy
        entropy = stats.entropy(prob_dist, base=2)

        return entropy


    # Entropy is maximized when each value in the signal is equally likely, 
    # which in the case of a uniform distribution, occurs when all 
    # values are distributed over the interval 
    # [# 𝑎# ,# 𝑏# ]
    # [a,b] with equal probability.
    # When you are dealing with a signal of 
    # 𝑛,  n elements (not just a single value), the total maximum entropy of 
    # the signal will indeed be the sum of the individual entropies for each element.

    def max_entropy(self, signal):
        # Number of possible distinct values
        mx = max(signal)
        mn = min(signal)
        n = len(signal)

        #assert mn==mx
        rang = mx - mn + 1
        # Entropy per element (discrete uniform distribution)
        entropy_per_element = math.log2(rang)
        # Total maximum entropy for n elements
        total_entropy = n * entropy_per_element
        return total_entropy  
    
    def info_content(self, signal):
        etp = self.calculate_entropy(signal, 10)
        max_etp = self.max_entropy(signal)
        etp_diff = max_etp - etp
        assert etp_diff >0
        
        return max_etp 



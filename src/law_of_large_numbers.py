import numpy as np
import matplotlib.pyplot as plt

# Simulating coin flips
def coin_flip_simulation(n):
    outcomes = np.random.randint(0, 2, size=n)
    averages = np.cumsum(outcomes) / (np.arange(1, n+1))
    return averages

n = 1000
averages = coin_flip_simulation(n)

# Plot
plt.plot(averages)
plt.axhline(y=0.5, color='r', linestyle='--')
plt.title('Law of Large Numbers')
plt.xlabel('Number of Flips')
plt.ylabel('Average')
plt.show()
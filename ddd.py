import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, bins=50, facecolor='r', alpha=0.75, density=True)
plt.xlabel('warotości')
plt.ylabel('prawdopodobieństwo wystątpienia')
plt.title('Histogram')
plt.grid(True)

plt.show()


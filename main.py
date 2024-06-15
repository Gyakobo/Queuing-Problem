import numpy as np
import matplotlib.pyplot as plt

x = [i for i in range(0, 10)]

plt.plot(x, np.random.exponential(x))
plt.show()

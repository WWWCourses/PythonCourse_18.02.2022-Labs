import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1,11, 10)
y = np.random.randint(20,31, 10)

# plot line using State-based interface:
plt.plot(x,y)

# to show the figure:
plt.show()

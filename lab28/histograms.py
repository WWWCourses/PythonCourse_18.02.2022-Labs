from turtle import color
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy.stats import norm


fig, ax = plt.subplots(2,2)

# x = np.linspace(1, 100, 100)
# print(x)
# ax[0][0].hist(x)
# ax[0][1].hist(x, bins=2)

# 1000 mens => heights 180 +-20
# [1,2,3,4,5]
# mean = 1+2+9+4+5=4.2
# median = 9

# x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
# ax[0][0].plot(x, norm.pdf(x), lw=2, linestyle=':', color="#F00", alpha=1, label='norm pdf')

xNorm = np.random.normal(180, 20, size=1000)
print(xNorm.min(), xNorm.max())
ax[0][0].hist(x=xNorm)
ax[0][0].grid(True, alpha=0.1,color='#F00')

plt.show()
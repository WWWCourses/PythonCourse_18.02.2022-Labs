import numpy as np
import matplotlib.pyplot as plt


mu, sigma = 170, 20 # mean and standard deviation
x = np.random.normal(mu,sigma,100).astype('int')
print(x.min(), x.max(), x)

fig,ax = plt.subplots(2,2)
ax[0][0].hist(x)
ax[1][0].hist(x,bins=20)
ax[0][1].hist(x,bins=200)
ax[1][1].bar(x,x)




plt.show()
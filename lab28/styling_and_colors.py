import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


fig, ax = plt.subplots()


a = 5
b = 10
c = 3
d = 10

x = np.linspace(-1,1, 30)
# y = np.sin(x)
y=a+b*np.sin(c*x+d)

ax.scatter(x,y, cmap='veridis')
ax.set_title('Demo Title', fontsize=50)

# TODO why not working
mpl.rcParams['font.size']=50

plt.show()
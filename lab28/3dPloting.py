from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# fig, ax = plt.subplots(2,2)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# set label
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# input date
# x = np.arange(1,11)
# y = x+2
# z = x+3

# ax.plot(x,y,z)

## try to plot spiral
# x = np.linspace(-1,1,24)
# y = np.sin(x)
# z = np.linspace(0,1,24)
# print(x.shape, y.shape, z.shape)

# ax.plot(x,y,z)
# ax.scatter(x,y,z, color='orange')

## from matplotlib docs
# Grab some test data.
# X, Y, Z = axes3d.get_test_data(0.05)
# ax.plot_surface(X, Y, Z, rstride=10, cstride=10)

# z = r**2 - (x**2 + y**2)
# try to plot sphere (x**2 + y**2 + z**2 = r2)
# r = 27
# x = np.arange(1,28)
# y = np.random.randint(1,28,27)
# z = np.sqrt(r**2 - (x**2 + y**2))

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x,y,z, color="#F00", cmap=)
# ax.plot(x,y,z)







plt.show()


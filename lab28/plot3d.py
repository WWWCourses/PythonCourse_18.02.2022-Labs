import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.axes3d import get_test_data


fig = plt.figure()
# define 3d plot:
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# define inputs:
x = np.arange(1,11)
z=y=x
## drow 3d line:
# ax.plot(x,y,z)

## drow 3d wireframe:
X = np.linspace(-10)
print(X.shape,Y.shape,Z.shape)
ax.plot_wireframe(X,Y,Z)


##

plt.show()
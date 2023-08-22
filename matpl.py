import matplotlib as plt
from Random_Walk import RandomWalk

rw = RandomWalk()

rw.fill_walk()

plt.scatter(rw.x_values,rw.y_values,s= 15)
plt.show()

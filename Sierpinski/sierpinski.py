import matplotlib.pyplot as plt
import random

plt.ion()

def mid_point(a, b, c, d, r):
    """
        Divides the line segment between the 2 points
        (a,b) and (c,d) by the ratio r

        returns the coordinates of the mid point
    """

    x = a + r * (c-a)
    y = b + r * (d-b)

    return x,y



anchors_x = [0, 100, 50]
anchors_y = [0, 0, 70]

plt.figure()
plt.scatter(anchors_x, anchors_y, marker='o', color='r')

current_x = 0
current_y = 0

num_loops = 100000
hx = [None] * num_loops
hy = [None] * num_loops

for k in range (0,num_loops):

    i = random.randint(0,len(anchors_x)-1)
    new_x, new_y = mid_point(current_x, current_y, anchors_x[i], anchors_y[i], 0.5)

    #plt.scatter(new_x, new_y, marker='.', color='k')

    current_x = new_x
    current_y = new_y
    
    hx[k] = current_x
    hy[k] = current_y

plt.scatter(hx, hy, marker = '.', color='k')


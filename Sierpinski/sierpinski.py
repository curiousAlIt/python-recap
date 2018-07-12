import matplotlib.pyplot as plt

def mid_point(a, b, c, d, r):
    """
        Divides the line segment between the 2 points
        (a,b) and (c,d) by the ratio r

        returns the coordinates of the mid point
    """

    x = a + r * (c-a)
    y = b + r * (d-b)

    return x,y


a = 6
b = 5
c = 94
d = 36

plt.ion()
plt.figure()
plt.scatter(a,b, marker='*', color = 'r')
plt.scatter(c,d, marker='+', color='g')

for k in range (1,10):
    
    xx,yy = mid_point(a,b,c,d, k/10.0)
    print('K is now %d - for this k the mid point is %f , %f ' % (k,xx,yy))
    
    plt.scatter(xx, yy, marker ='x', color = 'b')

print('Finished the loop')




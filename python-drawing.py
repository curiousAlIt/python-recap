import numpy as np
import matplotlib.pyplot as plt
plt.ion()

plt.figure()
#plt.hold('on')

plt.xlim([0, 300])
plt.ylim([0, 400])

plt.plot(50,120, 'rs')
plt.plot(100,100, 'b8')
plt.plot(150,120, 'go')
plt.plot(200,100, 'r1')

for x in np.arange(7.0, 20.0, 2.0):

    plt.plot(x, x*x, 'co')




plt.figure()
for r in [1, 2, 3, 4]:
    y = r*50
    for s in range(1, 2*r):
        x = 10*s
        plt.plot(x, y, 'bo')

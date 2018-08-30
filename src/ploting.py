## Important
## data ploting and visualization :

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.arange(10)
print(data)
plt.plot(data)

# to ploat a graph first need to create a figure window

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.plot(np.random.randn(50).cumsum(), 'k--')
ax3.plot(data)
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.random.randn(30), np.random.randn(30) + 3 * np.random.randn(30))
plt.show()

#plotting multiple subplots

fig, axis = plt.subplots(2,2, sharex=True, sharey=True)

for i in range(2):
    for j in range(2):
        axis[i, j].hist(np.random.randn(500), bins=50, color='R', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)
axis[1, 1].plot(np.random.randn(5).cumsum(), 'ko--')
plt.show()

#colors markers and line style

from numpy.random import randn
fig, axis = plt.subplots(2,2)
plt.plot(randn(20).cumsum(), linestyle='dashed', color='G', marker='o', drawstyle='steps-post')
axis[0, 0].plot(randn(20).cumsum(), linestyle='dashed', color='B', marker='o', label='step-post')
plt.legend('best')
plt.show()


fig, axis = plt.subplots(1,1)
axis.plot(randn(1000).cumsum())
tickes = axis.set_xticks([0, 250, 500, 750, 1000])
lables = axis.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
axis.set_title('My First Plot')
axis.set_xlabel('Stages')


# you can set same props to the y axis also but in different way
# there is a a handy function which will allow you to set the all props in one step
props = {
    'title': 'my first plot',
    'xlabel': 'stages',
    'ylabel': 'inches',
}

axis.set(**props)
plt.show()
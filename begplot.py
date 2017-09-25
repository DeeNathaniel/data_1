opening plots in matplot

# importing matplot numpy and pylab
import matplotlib
import numpy as np
import pylab as pl

# opening as empty plot
# need to import matplotlib, numpy and pylab
fig = plt.figure() 

fig.suptitle('No axes on this figure') #labels figure with 'No axes in this figure'

fig, ax_lst = plt.subplots(2, 2) # a figure with a 2x2 grid of Axes

fig, ax_lst = plt.subplots(1, 1) # figure with 1 grid

# linear, quadratic and cubic lines

x = np.linspace(0, 2, 100) # sets

plt.plot(x, x, label='linear') # linear line will label as linear  in legend
plt.plot(x, x**2, label='quadratic') # quadratic line will label as quad in legend
plt.plot(x, x**3, label='cubic') # cubic line label as cubic

plt.xlabel('x label') # labels x axis
plt.ylabel('y label') # labels y axis

plt.title("Simple Plot") labels graph

plt.legend() # labels the graph

plt.show() # i dunno what this is

# waves

x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.show()
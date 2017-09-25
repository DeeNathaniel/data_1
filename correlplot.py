#correlplot

csv = np.genfromtxt ('/home/dee/Documents/data_1/enhancedcorrelationonly.csv', delimiter = ",")
first = csv[:,0]
second = csv[:,1]
third = csv[:,2]
fourth = csv [:,3]
fifth = csv [:,4]


x = first
plt.plot (x)

plt.title('Enhanced Correlation data')
plt.ylabel('correlation')
plt.xlabel('images')
plt.legend()
plt.show()
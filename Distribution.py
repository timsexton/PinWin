from scipy import stats
import numpy as np
import csv
import os
import matplotlib.pyplot as plt
import pylab


#Variables
tableFolder = "PAPAtables"
scores_vals=[]

#To get columns
def column(matrix, i):
    return [row[i] for row in matrix]

#For each table file
for filename in os.listdir(tableFolder):
	scores_vals=[]
	fpath = os.path.join(tableFolder, filename)
	file = open(fpath, 'rb')
	reader = csv.reader(file,delimiter='\t')
	for line in reader:
		for i in range(2, len(line)-3):
			scores_vals.append(line[i])
			#print line[i]
			#print scores_vals
		
	scores_vals=scores_vals[1:]
	#print scores_vals
	scores_array = np.asarray(scores_vals)
	scores_array = scores_array.astype(np.float)
	
	#From this variable generate a histogram
	rvs = stats.lognorm.rvs(np.log(2), loc=0, scale=4, size=250) # Generate some random variates as data
	#print type(rvs)
	#print type(scores_array)
	#print scores_array
	n, bins, patches = plt.hist(scores_array, bins=50, normed=True) # Plot histogram

	shape, loc, scale = stats.lognorm.fit(scores_array, floc=0) # Fit a curve to the variates
	mu = np.log(scale) # Mean of log(X)
	sigma = shape # Standard deviation of log(X)
	M = np.exp(mu) # Geometric mean == median
	s = np.exp(sigma) # Geometric standard deviation

	# Plot figure of results
	x = np.linspace(scores_array.min(), scores_array.max(), num=400)
	plt.plot(x, stats.lognorm.pdf(x, shape, loc=0, scale=scale), 'r', linewidth=5) # Plot fitted curve
	ax = plt.gca() # Get axis handle for text positioning
	txt = plt.text(0.9, 0.9, 'M = %.2f\ns = %.2f' % (M, s), horizontalalignment='right', size='large', verticalalignment='top', transform=ax.transAxes)
	pylab.show()




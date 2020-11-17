import numpy as np
import matplotlib.pyplot as plt

#CHALLENGE 1
#creates an array of numbers in the given range
nums = np.arange(start=0, stop=21, step=1)

#using numpy functions to determine mean, std deviation, and variance
#of the above generated array of numbers
#as well as displaying them with an appropriate message
mean_nums = np.mean(nums)
print("Mean:",mean_nums)

std_dev = np.std(nums)
print("Standard Deviation:",round(std_dev,3))

variance = np.var(nums)
print("Variance",variance)

#CHALLENGE 2
nums_1 = [0.5, 0.7, 1.0, 1.2, 1.3, 2.1]
bins_1 = [0, 1, 2, 3]

#labels
plt.title("Histogram showing nums vs bins")
plt.xlabel("Nums")
plt.ylabel("Bins")

#histogram
plt.hist(nums_1, bins=bins_1, edgecolor='black')
plt.show()

import matplotlib.pyplot as plt 
import numpy as np
'''
#box plot
a = [1.3, 3.4, 2.3, 9.8]
b = [3.5, 4.9, 1.3, 2.2]
c = [9.7, 1.5, 4.3, 0.9, 11.2]

data1=[a, b, c]

plt.boxplot(data1)
plt.xlabel("Colleges")
plt.ylabel("scores")
plt.title("Boxplot for Colleges")
'''
plt.show()

#Scatter plot
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9])
y = np.array([99, 86, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.plot(x,y,'o')

m, b = np.polyfit(x, y, 1)

plt.plot(x, m*x + b)

plt.show()

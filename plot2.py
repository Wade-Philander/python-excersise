import matplotlib.pyplot as plt 
import numpy as np

a = np.array([14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 18.5])
b = np.array([200, 330, 190, 340, 410, 445, 415])
plt.plot(a, b,'o')

m,n = np.polyfit(a, b, 1)

plt.plot(a, m*a + n)

plt.xlabel("Temperature")
plt.ylabel("Price in  (R)")
plt.title("Soup sales in relation to temperature")

plt.show()

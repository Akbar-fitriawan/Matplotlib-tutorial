import numpy as np
import matplotlib.pyplot as plt

"""
    1. Membuat data
    2. Membuat Plot
    3. manampilkan Plot
"""

# Membuat data 
x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])
y2 = np.array([1,16,81,256,625])
# Membuat Plot
plt.plot(x,y)
plt.plot(x,y2)

# Menampilkan plot
plt.show()


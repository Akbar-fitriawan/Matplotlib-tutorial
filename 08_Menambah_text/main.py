import matplotlib.pyplot as plt
import numpy as np

# Membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

# Membuat plot
plt.plot(t,y)
plt.text(2,0.5, r'$ y = \mathcal{A}.sin(2 \omega t)$')
plt.text(2,0.4, r'$ \mathcal{A} = 1 cm, \omega = 1 HZ$')

# Menampilkan plot
plt.show()



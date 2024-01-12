import matplotlib.pyplot as plt
import numpy as np

# Membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

# Membuat plot
plt.plot(sudut,y)
plt.title('Grafik sinusoidal')
plt.text(190,1,'Magnituda')
plt.text(360,0.1,"sudut")

plt.yticks([-1,-0.5,0,0.5,1])
plt.xticks([0,90,180,270,360],
           [r'${0}^0$',r'${90}^0$',r'${180}^0$',r'${270}^0$',r'${360}^0$',])

ax = plt.gca()
ax.spines['left'].set_position(('data', 180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


# Menampilkan plot
plt.show()

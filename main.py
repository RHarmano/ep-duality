import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2*np.pi, 500, endpoint=True)
x = t
y = t
x,y = np.meshgrid(x,y)

f1 = 25
f2 = 2*f1
f3 = 2*f2

fig, ax = plt.subplots()
xdata, ydata = [], []
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(0, 1.1)
plt.title(r'RWA Simulation Animation for a Frequency of $\omega$ = %.2f Hz'%f1, size=18, weight='bold')
plt.xlabel('x', size=14, weight='bold')
plt.ylabel('y', size=14, weight='bold')
ax.set_xticks([0,np.pi/2,np.pi,3/2*np.pi,2*np.pi])
ax.set_xticklabels(['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'2$\pi$'])
ax.set_yticks([0,np.pi/2,np.pi,3/2*np.pi,2*np.pi])
ax.set_yticklabels(['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'2$\pi$'])

def update(frames):
    # xdata = t
    # # y1 = np.exp(-(t-frames)**2)*np.sin(f1*t)**2
    # y2 = np.exp(-(t-frames)**2)*np.sin(f2*t)**2
    # # y3 = np.exp(-(t-frames)**2)*np.sin(f3*t)**2
    # cont.set_data(xdata, y2)
    z = 1/(2*np.pi**0.5)*(np.exp(-((x-frames)**2+(y-frames)**2)))*(np.sin(f1*x)*np.sin(f1*y))
    # z = (np.sin(2*x/t.max()-frames)**2+np.sin(2*y/t.max()-frames)**2)
    cont = plt.contourf(x,y,z)
    return cont

ani = FuncAnimation(fig, update, frames=np.arange(start=0,stop=2*np.pi,step=np.pi/8), interval=10)
plt.show()

fig2, ax2 = plt.subplots()
xdata, ydata = [], []
ax2.set_xlim(0, 2*np.pi)
ax2.set_ylim(0, 1.1)
plt.title(r'Quantum Corral Pulse Simulation, Bounded by A Single Oscillation where $\omega$ = %.2f Hz'%f1, size=18, weight='bold')
plt.xlabel('x', size=14, weight='bold')
plt.ylabel('y', size=14, weight='bold')
ax2.set_xticks([0,np.pi/2,np.pi,3/2*np.pi,2*np.pi])
ax2.set_xticklabels(['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'2$\pi$'])
ax2.set_yticks([0,np.pi/2,np.pi,3/2*np.pi,2*np.pi])
ax2.set_yticklabels(['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'2$\pi$'])

# def corral():
#     return cont2
# z2 = 1/(2*np.pi**0.5)*(np.exp(-((x-np.pi)**2+(y-np.pi)**2)))*(np.sin(x-np.pi)+np.sin(y-np.pi))**2
# z2 =(np.sin(x-np.pi)*np.sin(y-np.pi))**2
# cont2 = ax2.contourf(x,y,z2)
# plt.show()
# ani.save('C:/Users/roman/Documents/corral.gif', writer='imagemagick', fps=60)
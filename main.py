import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2*np.pi, 500, endpoint=True)
f1 = np.pi
f2 = 2*f1
f3 = 2*f2

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'b-')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(0, 2)
    return ln,

def update(frames):
    xdata = t
    y1 = np.exp(-(t-frames)**2)*np.sin(f1*t)**2
    y2 = np.exp(-(t-frames)**2)*np.sin(f2*t)**2
    y3 = np.exp(-(t-frames)**2)*np.sin(f3*t)**2
    ln.set_data(xdata, y2)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(-t.max()/2, 2*t.max(), 500),
                    init_func=init, blit=True)
# plt.show()
ani.save('/RWA.mp4')
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

file = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test5/blackholes.pkl'


with open(file,'rb') as f:
    data = pickle.load(f)

#grep BHSink output.out
yay = data['data']

x1 = yay[0]['x']
y1 = yay[0]['y']
z1 = yay[0]['z']
time1 = yay[0]['Time']


x2 = yay[1]['x']
y2 = yay[1]['y']
z2 = yay[1]['z']
time2 = yay[0]['Time']


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_title("Black Hole Position")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.xlim([-15,20])
plt.ylim([-15,20])
ax.set_zlim([-15,20])
N = len(time1)
for i in range(N-1):
    p = ax.plot3D(x1[i:i+2], y1[i:i+2], z1[i:i+2], color=plt.cm.jet(i/N))

N2 = len(time2)
for j in range(N2-1):
    p2 = ax.plot3D(x2[j:j+2], y2[j:j+2], z2[j:j+2], color=plt.cm.jet(j/N2))


plt.show()
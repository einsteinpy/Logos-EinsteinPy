import numpy as np
import astropy.units as u
from einsteinpy.metric import Schwarzschild
import matplotlib.pyplot as plt
from einsteinpy import constant

# variables to be used for plotting
end_lambda=0.021
M = 5.972e24 * u.kg
start_time = 0 * u.s




# generate the white dot at centre
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(0,0, s=0.5, color='white')
plt.axis(xmin = -350, xmax=350, ymin=-350, ymax=350)
ax.set_aspect(1)
plt.savefig(fname='whitedot.png', transparent=True, dpi=1500)


# generate 1st Red-Purple Orbit
fig = plt.figure()
ax = fig.add_subplot(111)
pos_vec = np.array([200.0, np.pi/2, 0.5*(np.pi/2+(np.pi+np.pi/6))])
vel_vec = np.array([0, 0., 7600.])
cl = Schwarzschild.from_values(pos_vec, vel_vec, start_time, M)
ANS = cl.calculate_trajectory(end_lambda=end_lambda/30, OdeMethodKwargs={'stepsize':0.2e-6})
ans = ANS[1]
r = np.array([t[1] for t in ans])
print(r[-1])
phi = np.array([t[3] for t in ans])
time = np.array([t[0] for t in ans])
x = r * np.cos(phi)
y = r * np.sin(phi)
ax.scatter(x,y, s=0.4, c=time[::-1], cmap='RdPu')
ax.scatter(0,0, color='black')
plt.axis(xmin = -350, xmax=350, ymin=-350, ymax=350)
ax.set_aspect(1)
plt.savefig(fname='swoosh0.png', transparent=True, dpi=1500)


# generate 2nd Red-Purple Orbit
fig = plt.figure()
ax = fig.add_subplot(111)
pos_vec = np.array([200.0, np.pi/2, 0.5*(np.pi/2+(np.pi+np.pi/6))+2*np.pi/3])
vel_vec = np.array([0, 0., 7600.])
cl = Schwarzschild.from_values(pos_vec, vel_vec, start_time, M)
ANS = cl.calculate_trajectory(end_lambda=end_lambda/30, OdeMethodKwargs={'stepsize':0.2e-6})
ans = ANS[1]
r = np.array([t[1] for t in ans])
print(r[-1])
phi = np.array([t[3] for t in ans])
time = np.array([t[0] for t in ans])
x = r * np.cos(phi)
y = r * np.sin(phi)
ax.scatter(x,y, s=0.4, c=time[::-1], cmap='RdPu')
ax.scatter(0,0, color='black')
plt.axis(xmin = -350, xmax=350, ymin=-350, ymax=350)
ax.set_aspect(1)
plt.savefig(fname='swoosh1.png', transparent=True, dpi=1500)


# generate 3rd Red-Purple Orbit
fig = plt.figure()
ax = fig.add_subplot(111)
pos_vec = np.array([200.0, np.pi/2, 0.5*(np.pi/2+(np.pi+np.pi/6))+4*np.pi/3])
vel_vec = np.array([0, 0., 7600.])
cl = Schwarzschild.from_values(pos_vec, vel_vec, start_time, M)
ANS = cl.calculate_trajectory(end_lambda=end_lambda/30, OdeMethodKwargs={'stepsize':0.2e-6})
ans = ANS[1]
r = np.array([t[1] for t in ans])
print(r[-1])
phi = np.array([t[3] for t in ans])
time = np.array([t[0] for t in ans])
x = r * np.cos(phi)
y = r * np.sin(phi)
ax.scatter(x,y, s=0.4, c=time[::-1], cmap='RdPu')
ax.scatter(0,0, color='black')
plt.axis(xmin = -350, xmax=350, ymin=-350, ymax=350)
ax.set_aspect(1)
plt.savefig(fname='swoosh2.png', transparent=True, dpi=1500)


# generate Petal Orbit-1
fig = plt.figure()
ax = fig.add_subplot(111)
pos_vec = np.array([306.0, np.pi/2, -np.pi/6])
real_omega = 950.6962496328747
vel_vec = np.array([0, 0., real_omega])
cl = Schwarzschild.from_values(pos_vec, vel_vec, start_time, M)
ANS = cl.calculate_trajectory(end_lambda=end_lambda, OdeMethodKwargs={'stepsize':0.2e-6})
ans = ANS[1]
r = np.array([t[1] for t in ans])
print(r[-1])
phi = np.array([t[3] for t in ans])
time = np.array([t[0] for t in ans])
x = r * np.cos(phi)
y = r*np.sin(phi)
ax.scatter(x,y, s=0.4, c=time, cmap='GnBu')
ax.scatter(0,0, color='black')
plt.axis(xmin = -350, xmax=350, ymin=-350, ymax=350)
ax.set_aspect(1)
plt.savefig(fname='momo0.png', transparent=True, dpi=1500)


# generate Petal Orbit-2
fig = plt.figure()
ax = fig.add_subplot(111)
pos_vec = np.array([306.0, np.pi/2, np.pi/2])
real_omega = 950.6962496328747
vel_vec = np.array([0, 0., real_omega])
cl = Schwarzschild.from_values(pos_vec, vel_vec, start_time, M)
ANS = cl.calculate_trajectory(end_lambda=end_lambda, OdeMethodKwargs={'stepsize':0.2e-6})
ans = ANS[1]
r = np.array([t[1] for t in ans])
print(r[-1])
phi = np.array([t[3] for t in ans])
time = np.array([t[0] for t in ans])
x = r * np.cos(phi)
y = r*np.sin(phi)
ax.scatter(x,y, s=0.4, c=time, cmap='GnBu')
ax.scatter(0,0, color='black')
plt.axis(xmin = -350, xmax=350, ymin=-350, ymax=350)
ax.set_aspect(1)
plt.savefig(fname='momo1.png', transparent=True, dpi=1500)


# generate Petal Orbit-3
fig = plt.figure()
ax = fig.add_subplot(111)
pos_vec = np.array([306.0, np.pi/2, -5*np.pi/6])
real_omega = 950.6962496328747
vel_vec = np.array([0, 0., real_omega])
cl = Schwarzschild.from_values(pos_vec, vel_vec, start_time, M)
ANS = cl.calculate_trajectory(end_lambda=end_lambda, OdeMethodKwargs={'stepsize':0.2e-6})
ans = ANS[1]
r = np.array([t[1] for t in ans])
print(r[-1])
phi = np.array([t[3] for t in ans])
time = np.array([t[0] for t in ans])
x = r * np.cos(phi)
y = r*np.sin(phi)
ax.scatter(x,y, s=0.4, c=time, cmap='GnBu')
ax.scatter(0,0, color='black')
plt.axis(xmin = -350, xmax=350, ymin=-350, ymax=350)
ax.set_aspect(1)
plt.savefig(fname='momo2.png', transparent=True, dpi=1500)

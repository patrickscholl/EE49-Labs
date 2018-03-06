import pickle
import matplotlib
import numpy as np
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
data = pickle.load(open('power.pkl','rb'))
plt.figure()
plt.plot(data['R'], data['P'], '.')
plt.xscale('log')
plt.ylabel('Power [mW]')
plt.xlabel('Resistance [Ohms]')
plt.show()
plt.figure()
R = data['R']
P = data['P']
I = []
V = []
for i in range(len(R)):
	I.append(np.sqrt((P[i]*1000)/(R[i])))
	V.append(I[i]*R[i]/1000)
plt.plot(R, V, '.')
plt.ylabel('Voltage [V]')
plt.xscale('log')
plt.xlabel('Resistance [Ohms]')
plt.show()
plt.figure()
plt.plot(R, I, '.')
plt.xscale('log')
plt.ylabel('Current [mA]')
plt.xlabel('Resistance [Ohms]')
plt.show()
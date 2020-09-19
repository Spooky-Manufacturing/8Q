#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
from qutip import *
N=5
a=destroy(N) 
H=a.dag()*a     # Simple oscillator Hamiltonian
psi0=basis(N,1) # Initial Fock state with one photon
kappa=1.0/0.129 # Coupling rate to heat bath
nth= 0.063      # Temperature with <n>=0.063

# Build collapse operators for the thermal bath
c_ops = []
c_ops.append(np.sqrt(kappa * (1 + nth)) * a)
c_ops.append(np.sqrt(kappa * nth) * a.dag())

ntraj = [1,5,15,904] # number of MC trajectories
tlist = np.linspace(0,0.8,100)
mc = mcsolve(H,psi0,tlist,c_ops,[a.dag()*a],ntraj)
me = mesolve(H,psi0,tlist,c_ops, [a.dag()*a])

fig = plt.figure(figsize=(8, 8), frameon=False)
plt.subplots_adjust(hspace=0.0)

# Results for a single trajectory
ax1 = plt.subplot(4,1,1)
ax1.xaxis.tick_top()
ax1.plot(tlist,mc.expect[0][0],'b',lw=2)
ax1.set_xticks([0,0.2,0.4,0.6])
ax1.set_yticks([0,0.5,1])
ax1.set_ylim([-0.1,1.1])
ax1.set_ylabel(r'$\langle P_{1}(t)\rangle$')

# Results for five trajectories
ax2 = plt.subplot(4,1,2)
ax2.plot(tlist,mc.expect[1][0],'b',lw=2)
ax2.set_yticks([0,0.5,1])
ax2.set_ylim([-0.1,1.1])
ax2.set_ylabel(r'$\langle P_{1}(t)\rangle$')

# Results for fifteen trajectories
ax3 = plt.subplot(4,1,3)
ax3.plot(tlist,mc.expect[2][0],'b',lw=2)
ax3.plot(tlist,me.expect[0],'r--',lw=2)
ax3.set_yticks([0,0.5,1])
ax3.set_ylim([-0.1,1.1])
ax3.set_ylabel(r'$\langle P_{1}(t)\rangle$')

# Results for 904 trajectories
ax4 = plt.subplot(4,1,4)
ax4.plot(tlist,mc.expect[3][0],'b',lw=2)
ax4.plot(tlist,me.expect[0],'r--',lw=2)
plt.xticks([0,0.2,0.4,0.6])
plt.yticks([0,0.5,1])
ax4.set_xlim([0,0.8])
ax4.set_ylim([-0.1,1.1])
ax4.set_xlabel(r'Time (s)')
ax4.set_ylabel(r'$\langle P_{1}(t)\rangle$')

xticklabels = ax2.get_xticklabels()+ax3.get_xticklabels()
plt.setp(xticklabels, visible=False);
plt.show()

#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
from qutip.qip.device import Processor
from qutip.operators import sigmaz
proc = Processor(2)
proc.add_control(sigmaz(), cyclic_permutation=True)
proc.pulses[0].coeffs = np.array([[1.0, 1.5, 2.0], [1.8, 1.3, 0.8]])
proc.pulses[0].tlist = np.array([0.1,0.2,0.4,0.5])

proc.run()

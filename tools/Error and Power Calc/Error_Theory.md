# Connectivity

The connectivity graph shows all Qbits are connected to all other Qbits.
Connections are denoted as y, self is s.

Qbit|0|1|2|3|4|5|6|7
-------------------
0|s|y|y|y|y|y|y|y
1|y|s|y|y|y|y|y|y
2|y|y|s|y|y|y|y|y
3|y|y|y|s|y|y|y|y
4|y|y|y|y|s|y|y|y
5|y|y|y|y|y|s|y|y
6|y|y|y|y|y|y|s|y
7|y|y|y|y|y|y|y|s

# Motivation

Error analysis is important to understand the capabilities of our computer.
While Classical computers are deterministic, Quantum computers are probabilistic. This is a shift in thinking for a programmer, but can enable some minor speedups.
This probability makes it more difficult to determine the source of error and thus how to fix it, include with that the fragility of quantum states and the necessity of understanding where the errors propagate becomes apparent.

This document is provided to provide some transparency into my process, provide guidance and a reference as I develop and as an attempt to avoid this becoming an incomprehensible mess of code.
Quantum computing has the threefold difficulty of having low level assembly architecture while preforming in a very domain-specific area that is spread among many disciplines, and that list is rapidly growing.
As an open source project, these quantum computers are not expected to be in the hands of Quantum physicist or developers, but rather experimenters and hobbyists. This makes documentation more critical than other quantum projects.
This documentation will assist in fulfilling the Roadmap's Documentation success criteria.


# Error Calculations

This error analysis will be divided into two. There are four types of error: Preparation error, Gate error (Decoerance), Gate error and readout error.
There is not a way of testing the difference between preparation and readout error without working with the hardware, as we are not working with an SPS, the assumption can be that the error is nearly entirely preparation. Thus these two errors are combined into quantum-classical error (QC error).
Each algorithm will be run many times, probably 100 at the minimum, and our quantum results (Qr) will be compared against the expected results. We will use this to calculate the percent error with the following formula.
	(num_runs/num_incorrect)*100
This will be done for each Qbits or sets of Qbits in order to fill in various error charts. These charts will be used initially to experiment and lessen errors. As the compiler progresses these charts will also be used to guide the tranpiler in minimizing error in the computation.

Please note that at the initial stages the software will be in two parts, quantum and classical. The classical will be in python and fully implemented save for the importing of the data from the output of the QASM.

## Total Error

Total error can be modeled as follows where t is time:
	Err=QC+Gate+Qbit(t)
We measure this between two gates and fill in the ys in the connectivity graph at the top with our values. This is the value we want to minimize, the rest will provide the granularity we need to determine the best optimizations.
Total error will be directly measured using the Gate error.

## Decoerance/Qbit error

Decoerance is a function that I expect to be of the form where t is time:
	Decoerance = A+bt+ct^2
	It is possible to get further orders, but I do not expect more.
A is going to be a combination of some constant error for each Qbit, as well as QC error. Thus A = QC+a. Due to the lack of single photon source, we will assume that a is small.
We measure this by preparing all the Qbits, holding them for a time, then measuring. We must take into account the time taken between measurements.
i.e, if we say it takes nu milliseconds to measure a Qbit and we measure them in order, the time for Qbit n (Tn) is Tn=t+(nu*n)
We will then determine the function for each individual Qbit and fit a curve, as well as apply other statistics as needed.
Lastly we will do the same for all Qbits.

## Gate error

Gate error is the error created by the action of the gates. As CNOT error seems to be relatively standard for this function the implementation will focus on that.
Gate error will be found by finding the total error and subtracting out the rest. Thus we will perform a 2-qbit operation between each Qbit, subtract the Qbit error for the target where the time is the time taken to perform the 2-qbit gate.
After that we will look at the chart between expected and measured values.

## QC error

The Quantum-Classical error will be the majority of the error due to lack of a single photon source. Remember that Decoerance = QC+a+bt+ct^2. We will assume that the Qbit with the lowest QC+a has an a of zero and use that as our QC.
This is probably not correct, but it is a starting place that can be implemented in software.

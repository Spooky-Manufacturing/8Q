*************
Architecture
*************

Opcodes
========================================

Quantum Instructions
----------------------------------------
The 8Q Supports the following quantum operations with the opcodes:

Unitary Gates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+--------------+--------------------+--------+
| Operation |     Logic    | Digital Equivalent | OpCode |
+===========+==============+====================+========+
|  Pauli-X  |  0->1; 1->0  |        NOT         |        |
+-----------+--------------+--------------------+--------+
|  Pauli-Y  |  0->-i; i->0 |    NOT (Y axis)    |        |
+-----------+--------------+--------------------+--------+
|  Pauli-Z  |  1->0; 0->-1 |    NOT (Z axis)    |        |
+-----------+--------------+--------------------+--------+
|  Pauli-H  |Pi(Z), Pi/2(Y)|    RANDOM(0,1)     |        |
+-----------+--------------+--------------------+--------+


Other Quantum Gates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+----------------+--------------+--------------------+--------+
| Operation      |     Logic    | Digital Equivalent | OpCode |
+================+==============+====================+========+
|  Controlled-X  |  Q1 NOT Q2 X |     Q1 NOT Q2      |        |
+----------------+--------------+--------------------+--------+
|  Controlled-Y  |  Q1 NOT Q2 Y | Q1 NOT Q2 (Y axis) |        |
+----------------+--------------+--------------------+--------+
|  Controlled-Z  |  Q1 NOT Q2 Z | Q1 NOT Q2 (Z axis) |        |
+----------------+--------------+--------------------+--------+
|  Controlled-H  |   Q1 (x) Q2  |         None       |        |
+----------------+--------------+--------------------+--------+
|      SWAP      |    Q1-> Q2   |      Q1 <-> Q2     |        |
+----------------+--------------+--------------------+--------+
|     Measure    |   Qn -> 1,0; |         Yield      |        |
+----------------+--------------+--------------------+--------+

Digital Instructions
----------------------------------------------

Data Transfer
^^^^^^^^^^^^^^
move
load
store
    
DATA OPERATIONS:
Data Operations
^^^^^^^^^^^^^^^^^
add
add with carry
subtract
subtract with borrow
logical and
logical or
logical exclusive or
shift right
compare unsigned

Sequencing
^^^^^^^^^^^^^
jump
return
halt

Instruction

Hardware Architecture Issues For Programmers
============================================
When programming the 8Q it is important to remember these are physical qubits (photons) traversing a physical (optical) circuit, each instruction physically alters the path of the qubit through the circuit. Another very important fact to understand is that all of the gates within this processor are probabilistic, this is quite a bit unlike most programming you will have been acquainted with. What this means is sometimes the qubits will be destroyed during their transit through the processor, the workaround for this is to run a given algorithm multiple times, collect the results of your experiment, and then use classical arithmetic to confirm the answer.

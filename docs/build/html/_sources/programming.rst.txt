******************
Programming Guide
******************
The 8Q Programming Guide is designed to assist in the transition from digital only to digital/quantum programming.

Architecture Incompatibility
=============================
Thanks to modern programming languages, we are fairly well spoiled when it comes to things like cross-platform compatibility, unfortunately with quantum computing, this isn't the case. Every quantum processor manufacturer has their own personalized architecture. This has long been a source of pain in the digital world, and only recently have we begun moving towards universally compatible hardware, but unfortunately due to the differences in how bosonic, photonic, atomic, ionic, etc. quantum processors work, each needs its' own specialized instruction set to ensure smooth operation. For this reason we tend to make abstractions, from machine code to assembly, assembly to compiler, compiler to interpreter. Currently there are a few different assembly languages competing for adoption, but we've designed our first 8 qubit quantum processor with an eye towards a slightly reduced version of OpenQASM.

8Q Pre-processing: Why?
============================
8Q is different from the non-quantum processors you may be used to working with in that we use probabilistic gates, the biggest drawback is each gate introduces a possibility of losing a qubit. The way we get around this is by running a given program multiple times, collecting the results, and then testing the results via a classical processor to find the answer. To that end, the processor has a built-in pre-processor which calculates the success rate of a given algorithm and determine the time required to generate a correct answer, this pre-processor can be enabled/disabled as needed by setting the pre-processor flag to 1.
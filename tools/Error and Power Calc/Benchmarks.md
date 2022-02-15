# Benchmark Introduction and Motivation

We need a way of quantifying the power of our quantum computers. Qbit count was the initial measurement, but that's insufficient. A very noisy computer with millions of Qbits can be less useful than a less noisy, but smaller computer.
Ionq has a decent paper on this issue (https://ionq.com/posts/october-18-2021-benchmarking-our-next-generation-system). However their recommended algorithms are not general purpose. They do benchmark common algorithms, but their computers are annealers, not general purpose.
The 8Q project is focusing on general purpose computers. Thus we cannot expect them to stand up to either the commercial general purpose systems, and especially not the results from the specific algorithm computers shown in the whitepaper.
Although we could run the comparisons outlined by Ionq, each computer will be different. In the future those algorithms could be implemented and added, but for now the generalized benchmarks will suffice. (If you don't think so, it's an Open source project. Fix it.)

This document is provided to provide some transparency into my process, provide guidance and a reference as I develop and as an attempt to avoid this becoming an incomprehensible mess of code.
Quantum computing has the threefold difficulty of having low level assembly architecture while preforming in a very domain-specific area that is spread among many disciplines, and that list is rapidly growing.
As an open source project, these quantum computers are not expected to be in the hands of Quantum physicist or developers, but rather experimenters and hobbyists. This makes documentation more critical than other quantum projects.
This documentation will assist in fulfilling the Roadmap's Documentation success criteria.

## Qbit Count
### 8 Qbits

Just counting Qbits is the first, quickest and easiest way to attempt to quantify a computer's performance. The design we are creating has eight.

## CLOPS
## See question #25 on GitHub

CLOPS stands for Circuit Level Operations per Second. In other words, how many gates can be executed a second. Yes, this is hertz. This is probably to distinguish between the computer's speed and the frequencies needed to communicate with the qbit.
The maximum CLOPS will be determined by the slowest part in our gate and controller setup. The question has been raised on GitHub, question #25.

## Quantum Volume
## Depends on build. Benchmarking software in progress.

See https://medium.com/qiskit/what-is-quantum-volume-anyway-a4dff801c36f for more information.
Quantum volume is a way to measure how many Qbits a quantum computer can use effectively by identifying the largest square shaped circuit that can be effectively run on the device. We use the Heavy output generation problem to find this.
First we take n Qbits, and implement the Heavy output Generation algorithm for it. Then we run it and output heavy strings passing with probability of at least 2/3 and confidence better than 97.725%. Then we repeat with n+1 until we run out of Qbits or the test fails.
Last we find QV=2^(lastNToPass). A quick use of a calculator reveals that the theoretical maximum for our 8-qbit quantum computer is 2^8=256. This is quite a bit larger than IBM's most powerful computer with a quantum volume of 128.
With a lack of data, a QV of zero is probably to be expected. Noise canceling, incresing CLOPS, and other hardware improvements should improve this.
It's going to be a lot of work, but the existence of an affordable quantum computer is a great improvement!

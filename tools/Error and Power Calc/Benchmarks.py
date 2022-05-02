#For further explanation see Benchmarks.md


import Error_Cals.qasam as qasam
import time

def qbit_count():
    #hardcoding this in, would like to have this like a -h option.
    return 8

def clops():
    #We want to count how many operations we can do per second. Thus we time how long it takes to do a basic gate, then do math to figure out how many can be done per second.
    Start=time.clock()
    #since all the gates are the same, any cnot should take the same time.
    #TODO Should I do a lot of these and avg the times?
    qasam.CNOT(0,1)
    End=time.clock()
    T=End-Start
    F=1/T
    return F

def QV():
    # This is going to be rough, The individual steps are going to take some work and there are 6.
    # adapted from https://qiskit.org/textbook/ch-quantum-hardware/measuring-quantum-volume.html
    # Need to do research for the details. yay

    QVseq=generateQVSeq()
    IdealOut=simIdealOut()
    HeavOut=calcHeavOut()
    Noise=defineNoise()
    GateFid=avgGateFidelity()
    MaxDepth=calcMaxDepth()
    return calcQuantVol()



def generateQVSeq():

    # qubit_lists: list of list of qubit subsets to generate QV circuits
    qubit_lists = [[0,1,2],[0,1,2,3],[0,1,2,3,4],[0,1,2,3,4,5],[0,1,2,3,4,5,6],[0,1,2,3,4,5,6,7]]
    # ntrials: Number of random circuits to create for each subset
    ntrials = 100

    #and here the function dies because I don't know what the qv_circuit is
    return NotImplementedError


def simIdealOut():
    return NotImplementedError
def calcHeavOut():
    return NotImplementedError
def defineNoise():
    return NotImplementedError
def avgGateFidelity():
    return NotImplementedError
def calcMaxDepth():
    return NotImplementedError
def calcQuantVol():
    return NotImplementedError
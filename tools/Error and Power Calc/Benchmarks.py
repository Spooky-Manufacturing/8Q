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




    return NotImplementedError
#For further explanation see Error_Theory.md

import Error_Cals.qasam as qasam
import time


def qc_err():
    return NotImplementedError

def gate_err():
    return NotImplementedError

def Qbit_err():
    return NotImplementedError

def total_err(q, runs):
    #This should do. I don't know how communication with the qbits will be worked out. Will watch.
    #I'll need to implement the timing.
    total_err=[]
    for i in q:
        line_err=[]
        for j in q:
            #If the qbits are the same.....
            if i == j:
                line_err.append(-1)
                #....We append -1

            #If they are diffrent...
            else:
                k=0
                wrong=0
                #....We run a lot of CNOTS and do our error calculation
                while k<=runs:
                    Class=CNOT(i,j) #we know Class is right.
                    Quant=qasam.CNOT(i,j) #Quant will have the errors

                    if Class != Quant:
                        wrong +=1

                    k+=1
                line_err.append((wrong/runs)*100)

        total_err.append(line_err)

    return total_err


def CNOT(q1,q2):
    if q1==True:
        q2= not q2

    return q1,q2
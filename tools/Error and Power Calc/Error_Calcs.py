#For further explanation see Error_Theory.md

import Error_Cals.qasam as qasam
import time


def qc_err():
    #Need to figure out delay in qsam
    return NotImplementedError

def gate_err(q,runs):
    #Gate error= total error - Qbit error for the gate.
    #Run the functions required to get the errors needed.
    tot=total_err(q,runs)
    QErr=Qbit_err()

    #Setup the required variables
    gateErr=[]
    i=0
    j=0

    #Start the math. I think there is a easier way in python, but I'm mostly a C++ dev and so I'm used to just buildng the thing and python makes that easy anyway.
    while i<len(tot):
        gateErr0=[]
        while j<len(tot[i]):
            gateErr0.append(tot[i][j]-QErr[i][j])
            j+=1
        i+=1
        gateErr.append(gateErr0)
            
    return gateErr

def Qbit_err():
    #need to figure out delay in qsam.
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
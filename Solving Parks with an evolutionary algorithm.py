#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 13:48:08 2018

@author: david
"""
import numpy as np
import random
import copy
import Loadparksdata

#Generate a number of random solution for a certain problem
def gensols(nsols,matches):
    sols = []
    for n in range(nsols):
        sol = []
        for i in range(len(matches)):
            sol.append(random.choice(matches[i][0]))
        sols.append(sol)
    return sols

#Check how good a solution is. The correct solution has 0 errors.
def checkqual(sol):
    error = 0
    sidelength = len(sol)
    sollength = sidelength * sidelength
    for point in sol:
        #print(point)
        downward = int((sollength-point)/sidelength)
        upward = (sidelength - 1) - downward
        for i in range(downward):
            #print((i+1)*4 + point)
            if ((i+1)*sidelength+point) in sol:
                #print(808)
                error +=1
        for i in range(upward):
            #print(point - (i+1)*4)
            if (point - (i+1)*sidelength) in sol:
                error +=1
                #print(808)
        leftward = point % sidelength
        rightward = sidelength-1 - leftward
        for i in range(leftward):
            #print("left")
            #print(point - i -1 )
            if (point - i - 1) in sol:
                #print(808)
                error += 1
        for i in range(rightward):
            #print(point + i + 1)
            if (point + i + 1) in sol:
                #print(808)
                error += 1
        if downward >0 and rightward>0:
            #print(point+5)
            if (point+sidelength +1) in sol:
                error += 1
        if downward >0 and leftward>0:
            #print(point+3)
            if (point+sidelength -1) in sol:
                error += 1
        if upward >0 and rightward >0:
            if (point-sidelength+1) in sol:
                error += 1
        if upward >0 and leftward >0:
            if (point-sidelength-1) in sol:
                error +=1
    return(int(error/2))

#Load problems from file
def genprobs():
    probs = Loadparksdata.loaddata() 
    convproblems = []
    for n in range(len(probs)):
        temp = np.array(probs[n])
        #print(len(temp))
        matches = []
        for i in range(int(np.sqrt(len(temp)))):
            matches.append(np.where(temp==i))   
        convproblems.append(matches)
    return convproblems

#Go through the evolutionary cycle once
def cycleonce(sols,matches):
    quals = []
    targetlength = len(sols)
    for i in range(targetlength):
        errors = checkqual(sols[i])
        if errors == 0:
            #print(sols[i])
            return(sols[i])
        quals.append(errors)
    sortsols = sorted(zip(quals,sols))
    newsols = []
    
    #stochastic selection
    while len(newsols) < int(targetlength/2):
        candidate = random.choice(sortsols)
        if random.randint(0,10) > candidate[0]:
            newsols.append(candidate[1])
    
    #Non-stochastic selection- best half
#    i=0
#    while len(newsols) < int(targetlength/2):
#        newsols.append(sortsols[i][1])
#        i+=1
    
    #crossover
    while len(newsols) <targetlength:
        can1 = copy.copy(random.choice(newsols))
        can2 = copy.copy(random.choice(newsols))
        newcan = copy.copy(can1)
        for l in range(len(can1)):
            if(random.randint(0,1)==1):
                newcan[l] = can2[l]
                can2[l] = can1[l]
        newsols.append(newcan)
        newsols.append(can2)
    
    #mutation
    for sol in newsols:
        for n in range(len(sol)):
            if random.randint(1,8)==1:
                sol[n] = random.choice(matches[n][0])

    return(newsols)

#Run through the cycle a desired number of times
def run(maxcycles,init,matches):
    test = init
    n=0
    while(len(test) != len(matches)):
        test = cycleonce(test,matches)
        n+=1
        if n > maxcycles:
            return("failure")
    return(n)
    return(test)


  

#A bit of script to run the program. Does not return the solutions, but the number of cycles neccesary to reach it
#Fails is the important factor here - hpw many problems can be solved succesfully
avgd = []
allprob = genprobs()
fails = 0
for i in range(1): #How many repeats
    for n in range(len(allprob)):
        sols = gensols(100,allprob[n])
        outcome = run(100,sols,allprob[n])
        if outcome == "failure":
            fails += 1
        else:
            avgd.append(outcome)
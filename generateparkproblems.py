#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:53:10 2018

@author: david
"""
import copy
import random as rd

#The are only two possible correct solutions to this problem
#It is made sure that one of these is applicable to the current problem, while the other is not
solshape1 = [1,7,8,14]
solshape2 = [2,4,11,13]

sollist = []

sol1 = [0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0]
sol2 = [0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0]

defaultlist = [0] * 16

#Randomly create a problem
def fillbox(prob,problist): 
    for i in range(16):
        prob[i] = rd.randint(1,4)
    if testprob(prob) == True:
        problist.append(copy.copy(prob))
        
#See if this problem has a unique solution        
def testprob(prob):
    if testset(prob,solshape1)  ^ testset(prob,solshape2):
        if testset(prob,solshape1):
            sollist.append(sol1)
        else:
            sollist.append(sol2)
        return True
    else:
        return False

#Test if a particular problem matches a particular solution
def testset(prob,solshape):
    points = [prob[i] for i in solshape]
    if len(set(points)) == 4:
        return True
    else:
        return False

#Generate a number of problems, using the other methods
def genprobs(max):
    problist = []
    while len(problist) < max:
        fillbox(defaultlist,problist)
    comblist = list(zip(sollist,problist))
    rd.shuffle(comblist)
    return comblist
    probs, sols = zip(*comblist)

"""
@author: Yahel
"""
#What i would do in this situation is run through  
#the price list and calculate the loss. 
#I would store the max value of the loss and compare
#this to the value currently being calculated

import numpy as np
import random

#create a small test array
pricesLst1 = [[random.randint(1,100),random.randint(1,100)] for i in range(10)]

def return_largest_loss(pricesLst):
    maxLoss = 0
    for i in range(np.size(pricesLst,0)):
        loss = pricesLst[i][1] - pricesLst[i][0]      
        if loss > maxLoss:
            maxLoss = loss
    print(maxLoss)
        
return_largest_loss(pricesLst1)
#Exception i would test for would be if values are
#missing from the table the table        
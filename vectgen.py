##This function computes a vector a for a given symmetric matrix
#element of the vector should be n(n+1)/2
#Author- Aniruddha Roy, Department of Electrical Engineering, mail-ee18d031@smail.iitm.ac.in
#
#
#import numerical python library
import numpy as np

def vectgen(mat):
    #n = max(np.shape(mat))
    #vect = np.zeros((int(n*(n+1)/2)))
    n=len(mat) #length of the given matrix 
    vect = []
    for i in range(n):
        vect.append(mat[i,i:n+1].tolist()) #appending each row wise 
        
    vect = sum(vect,[]) #to make a nested list to normal list
    return np.array(vect).T

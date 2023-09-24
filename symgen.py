##This function computes a symmtric matrix for a given vector
#element of the vector should be n(n+1)/2
#Author- Aniruddha Roy, Department of Electrical Engineering, mail-ee18d031@smail.iitm.ac.in
#
#
#import numerical python library
import numpy as np

##### function to generates a symmetric matrix#####
def symgen(vect): #define the function
    n=int(0.5*(np.sqrt(1+8*len(vect))-1))
    vect = vect.T
    mat=[]; 
    mat.append(vect[0:n].tolist()); #first row 
    ind = n;
    
    for i in range(1,n):
        tempvect=np.zeros((1,i)).tolist() #make array to list 
        tempvect.append(vect[ind:ind+n-i].tolist()) #append zeros 
        tempvect=sum(tempvect,[]) #to make a nested list to normal list
        mat.append(tempvect)
        #mat.append((np.zeros((1,i)).tolist()).append(vect[ind:ind+n-i+1].tolist()))
        ind = ind+n-i
    

    mat = np.array(mat,dtype='float')
    for i in range(n):
        mat[i,i]=0.5*mat[i,i] #1/2 of each diagonal elements 

    mat = mat+mat.T #symmteric matrix 

    return mat

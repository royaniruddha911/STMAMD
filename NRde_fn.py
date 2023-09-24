##This Python code is for solving Riccati Diffferential equations for N players case.
#Author- Aniruddha Roy, Department of Electrical Engineering, mail-ee18d031@smail.iitm.ac.in 

#python librarry 
import numpy as np
# call symgen and vectgen
from symgen import symgen
from vectgen import vectgen

def NRde(t, y, N, S, Q):
    dy = np.zeros(len(y))
    L = len(y) // N
    Acl = np.zeros((2*N, 2*N))
    P=np.zeros((N,2*N,2*N))
    
    for k in range(N):
        P[k,:,:] = symgen(y[k*L:(k+1)*L]) #P matrix for each players
        #print(P[k,:,:])
        Acl = Acl - S[k,:,:]@P[k,:,:] #closed loop matrix 
        #print(Acl)
    for k in range(N):
        dy[k*L:(k+1)*L] = -vectgen(Acl.T@P[k,:,:]+P[k,:,:]@Acl+Q[k,:,:]+P[k,:,:]@S[k,:,:]@P[k,:,:])
        #print(dy)
        #Acl'*Pi+Pi*Acl+Q+Pi*Si*Pi
    
    return dy



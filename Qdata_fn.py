##This Python code- will give the current mode of the game (that is interception or rescue) and minimum distance defenders to each attackers 
#Author- Aniruddha Roy, Department of Electrical Engineering, mail-ee18d031@smail.iitm.ac.in 

#Pthon libraries 
import numpy as np
from sympy import symbols, hessian

def Qdata(Active,mode,amap):
    N=int(Active['N'])
    IN=np.identity(N)
    I2=np.identity(2)

    # Extract data from Active
    Attackers = Active['Na'][Active['epoch']] #Active Atatckers set
    Defenders = Active['Nd'][Active['epoch']] # Active Defenders set
    Target = Active['Nt'][Active['epoch']] # Active target set
    # # Initialize symbolic variables

    ################################Symbolic statevariables ################################################
    symbols_player = []
    for i in range(len(Attackers)):
        s = f'xa{i}'
        symbols_player.append(symbols(s)) # creating state variables symbolically for attackers 
        
    for i in range(len(Defenders)):
        s = f'xd{i}'
        symbols_player.append(symbols(s)) # creating state variables symbolically for defenders
        
    for i in range(len(Target)):
        s = f'xt{i}'
        symbols_player.append(symbols(s)) # creating state variables symbolically for target

    
    #######################################################################
    X = np.array(symbols_player)
    Xa=X[0:len(Attackers)] #attackers state variables 
    Xd=X[len(Attackers)+0:len(Attackers)+len(Defenders)] #defenders state variables 
    Xt=X[len(Attackers)+len(Defenders)+0:len(Attackers)+len(Defenders)+len(Target)] #target state variables 

    Q=np.zeros((N,2*N,2*N))
    #we are not multiplying I2 using Kron, so size of the matrix (N,N)

    ########Defenders to attackers and target###########
    Qda=np.zeros((len(Defenders),N,N))  #defenders to attackers# 
    Qdt=np.zeros((len(Defenders),N,N))  #defenders to target #
    for k in range(len(Defenders)):
        Qda[k,:,:] = 0.5 * hessian(sum((Xd[k] - Xa) ** 2), X)
        Qdt[k,:,:] = 0.5 * hessian(sum((Xd[k] - Xt) ** 2), X)
        Qda[k,:,:] = np.array(Qda[k,:,:]).astype(float)
        Qdt[k,:,:] = np.array(Qdt[k,:,:]).astype(float)
    ########## Target to defenders and Attackers ############
    Qtd=0.5 * hessian(sum((Xd - Xt) ** 2), X) #target to defenders 
    Qta=0.5 * hessian(sum((Xa - Xt) ** 2), X) # target to attackers
    Qtd=np.array(Qtd).astype(float)
    Qta=np.array(Qta).astype(float)

    ########## Attacker to Min. diatance defender and a Target######
    Qat=np.zeros((len(Attackers),N,N)) #attacker to target
    Qad=np.zeros((len(Attackers),N,N)) #attacker to defender 

    for k in range(len(Attackers)):
        Qad[k,:,:]=0.5 * hessian((Xa[k]-Xd[amap[k]])**2,X)  #Attacker to Min. diatance defender
        Qat[k,:,:] = 0.5 * hessian(sum((Xa[k] - Xt) ** 2), X) #attacker to target
        Qad[k,:,:] = np.array(Qad[k,:,:]).astype(float)
        Qat[k,:,:] = np.array(Qat[k,:,:]).astype(float)
        
    if mode == 1: #intercept 
       lambda_var=1 #non-suicidal attacker
       for k in range(len(Attackers)):
           Q[k,:,:]=np.kron((-lambda_var*Qad[k,:,:]+Qat[k,:,:]),I2) # Active attackers Qi
       for k in range(len(Defenders)):
           Q[len(Attackers)+k,:,:]=np.kron(Qda[k,:,:],I2) # Active defenders Qi
       for k in range(len(Target)):
           Q[len(Attackers)+len(Defenders)+k,:,:]=np.kron(-Qta,I2) #Active Target Qi
    else: #rescue mode
        mu=1
        for k in range(len(Attackers)):
            Q[k,:,:]=np.kron(Qat[k,:,:],I2) # Active attackers Qi
        for k in range(len(Defenders)):
            Q[len(Attackers)+k,:,:]=np.kron(Qdt[k,:,:],I2) # Active defenders Qi
        for k in range(len(Target)):
            Q[len(Attackers)+len(Defenders)+k,:,:]=np.kron((mu*Qtd-Qta),I2) #Active Target Qi
            
    return Q


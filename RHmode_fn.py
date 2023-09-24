##This Python code- will give the current mode of the game (that is interception or rescue) and minimum distance defenders to each attackers 
#Author- Aniruddha Roy, Department of Electrical Engineering, mail-ee18d031@smail.iitm.ac.in 

#python librrary 
import numpy as np
# Active = {} # define the dictionary Active 
# Active['Na'] = [[0, 1, 2, 3]] #number of active attackaers #nested list
# Active['Nd'] = [[0, 1, 2]] # number of active defenders 
# Active['Nt'] = [[0]]
# Active['epoch'] = 0
# Active['N'] = len(Active['Na'][Active['epoch']]) + len(Active['Nd'][Active['epoch']]) + len(Active['Nt'][Active['epoch']])
# Active['maxNa'] = 4 #maximum number of atatckers 
# Active['maxNd'] = 3 #maximum number of defenders 
# Active['epochflag'] = 0 # current epside=0, means no capture/interception/ rescue

# # initialize Players
# Players = {} #define dictionary Players 
# Players['ra'] = [0.8, 0.8, 0.8, 0.8] 
# Players['rd'] = [1, 1, 1]
# Players['rt'] = [1.2]
# Players['cra'] = [0.1, 0.1, 0.1]
# Players['crd'] = [0.1, 0.1, 0.1]
# Players['kappa'] = 6
# Players['delta'] = 0.01
# Players['T'] = 3
# # Intial conditions-initialize X0
# X0=np.array([ [-3.9218], [-0.3954], [-2.4157],[ 5.8160],[1.6504], [2.7579], [-2.1164], [-0.9372],[ -0.5449],[2.1968],[-0.5557],[1.4031],[ -4.1036], [-0.7077],[ -1.6472],[ -3.1541]])

def RHmode(posX, Active, Players):
    pos_X = np.reshape(posX, (int(len(posX)/2),2)).T   # reshaping the position 
    #print(pos_X)
    Xa = pos_X[:, Active['Na'][Active['epoch']]]  # attackers position vector 
    #print(Xa)
    Xd = pos_X[:, int(Active['maxNa'])+np.array(Active['Nd'][Active['epoch']])] #defenders position vector
    #print(Xd)
    Xt = pos_X[:, int(Active['maxNa']+Active['maxNd'])+np.array(Active['Nt'][Active['epoch']])] #target position vector
    #print(Xt)
    DISTAD = np.ones((Active['maxNa'], Active['maxNd'])) #Distance matrix- attackers and defenders 
    DISTAT = np.ones((Active['maxNa'], 1)) # Distance matrix-attackers and target
    Attackers = Active['Na'][Active['epoch']] #Active attackers for current episode 
    Defenders = Active['Nd'][Active['epoch']] # Active defenders for current episode
    # Follwoing, we will compute the DISTAD and DISTAT matrices 
    for k in range(len(Active['Na'][Active['epoch']])):
        for m in range(len(Active['Nd'][Active['epoch']])):
            DISTAD[Attackers[k], Defenders[m]] = np.linalg.norm(Xa[:, k]-Xd[:, m])  #Distance matrix- attackers and defenders
        DISTAT[Attackers[k]] = np.linalg.norm(Xa[:,k]-Xt.T) # Distance matrix-attackers and target
    amap = np.zeros(len(Active['Na'][Active['epoch']]), dtype=int)
    #Following- we compute the minimum distnace distance defenders for each attackers 
    for k in range(len(Active['Na'][Active['epoch']])):
        amap[k] = np.argmin(DISTAD[Attackers[k], Active['Nd'][Active['epoch']]]) #amap-minimum distnce defender for each atatcker
    ## based on the following condition-which is written in the if statement, current mode of the game will decide
    if np.min(DISTAT) < Players['kappa']*np.max(Players['cra']):
        mode = 1 #intercept
    else:
        mode = 0 #rescue
    #return mode, amap, DISTAD , DISTAT
    return mode, amap



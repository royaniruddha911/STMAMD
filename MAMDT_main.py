##This is the main Python code for Receiding Horizon implemenattion for Mutiple Attackers, Multiple defenders and one target
#Author- Aniruddha Roy, Department of Electrical Engineering, mail-ee18d031@smail.iitm.ac.in 
#import numpy package 
import numpy as np
import csv
# import the funtions from the python file
from scipy.linalg import expm
from RHmode_fn import RHmode
from RHstep_fn import RHstep
from gmterm_fn import gmterm
from newAcl_fn import expandAcl
from plotdata_fn import plotdata
from initialData_fn import initialData
# initialize Active
Active = {} # define the dictionary Active 
Active['Na'] = [[0, 1]]#number of active attackaers #nested list #change here 
Active['Nd'] = [[0, 1]] # number of active defenders  #change here
Active['Nt'] = [[0]]
Active['epoch'] = 0
Active['N'] = len(Active['Na'][Active['epoch']]) + len(Active['Nd'][Active['epoch']]) + len(Active['Nt'][Active['epoch']])
Active['maxNa'] = 2 #maximum number of atatckers 
Active['maxNd'] = 2 #maximum number of defenders 
Active['maxN']= Active['maxNa'] +Active['maxNd']+1
Active['TERMflag'] = 0
Active['epochflag'] = 0
Active['eventflag'] = 0

# Intial conditions-initialize X0
#X0 = 2 * np.random.randn(2 * (Active['maxNa'] + Active['maxNd'] + 1), 1)

# initialize Players
Players = {} #define dictionary Players 
Players['ra'] = [0.8, 0.8] #scaling factor of the control weight matrices  of the attackers
Players['rd'] = [1, 1] #scaling factor of the control weight matrices  of defenders
Players['rt'] = [1.2] #scaling factor of the control weight matrix of the target
Players['cra'] = [0.1, 0.1, 0.1] #capture radius of the attackers
Players['crd'] = [0.1, 0.1] #capture radius of the defenders 
Players['kappa'] = 6
Players['delta'] = 0.01 #sampling instatnt
Players['T'] = 3 #time horizon 

##########################################################################################
# field names 
if Active['maxNa'] == 2 and Active['maxNd'] == 2:
   fields = ['x--a0','y--a0','x--a1','y--a1','x--d0','y--d0','x--d1','y--d1','x--t0','y--t0']      
   file1 = "TrajectoryData.csv" # name of csv file which stores the trejectory data
   
if Active['maxNa'] == 3 and Active['maxNd'] == 2:
   fields = ['x--a0','y--a0','x--a1','y--a1','x--a2','y--a2','x--d0','y--d0','x--d1','y--d1','x--t0','y--t0']      
   file1 = "TrajectoryData.csv" # name of csv file which stores the trejectory data
   
   
if Active['maxNa'] == 2 and Active['maxNd'] == 3:
   fields = ['x--a0','y--a0','x--a1','y--a1','x--d0','y--d0','x--d1','y--d1','x--d2','y--d2','x--t0','y--t0']      
   file1 = "TrajectoryData.csv" # name of csv file which stores the trejectory data

         
if Active['maxNa'] == 3 and Active['maxNd'] == 3:
   fields = ['x--a0','y--a0','x--a1','y--a1','x--a2','y--a2','x--d0','y--d0','x--d1','y--d1','x--d2','y--d2','x--t0','y--t0']      
   file1 = "TrajectoryData.csv" # name of csv file which stores the trejectory data

   
if Active['maxNa'] == 4 and Active['maxNd'] == 3:
   fields = ['x--a0','y--a0','x--a1','y--a1','x--a2','y--a2','x--a3','y--a3','x--d0','y--d0','x--d1','y--d1','x--d2','y--d2','x--t0','y--t0']      
   file1 = "TrajectoryData.csv" # name of csv file which stores the trejectory data
  
   
if Active['maxNa'] == 3 and Active['maxNd'] == 4:
   fields = ['x--a0','y--a0','x--a1','y--a1','x--a2','y--a2','x--d0','y--d0','x--d1','y--d1','x--d2','y--d2','x--d3','y--d3','x--t0','y--t0']      
   file1 = "TrajectoryData.csv" # name of csv file which stores the trejectory data
##########################################################################################
#X0 = 2 * np.random.randn(2 * (Active['maxNa'] + Active['maxNd'] + 1), 1)  # initial condition
##################--------------------------##################
x = np.zeros((2*Active['maxN'],1))
Xinit=initialData(Active) #calling the Initial Data function 
# 2-2-1 index 0-6, # 2-IC, 5-II
# 3-2-1 index 0-10, # 3-IC,8-III, 9-C, 10-R
# 2-3-1 index 0-10, # 5-IC,8-II,  3-C, 10-IR
# 3-3-1 index 0-4
# 4-3-1 index 0-4 
# 3-4-1 index 0-3 #0-R,2-C, 3-III(d)

indx = 6 #which initial condition we want to select, change here 
Xinit[indx] = [2*Xinit[indx][i]+ 11/2 for i in range(len(Xinit[indx]))]
x[:] = Xinit[indx] # set the first column of x to the initial condition
xfin = Xinit[indx]
RH = 20 #receiding horizon
RHsteps = 50 #receiding horizon steps
terminalflag = 0
epochflag = 0 #episode 
xcnt = 0 #x count
# x[:, 0] = X0[:, 0]
# xfin = x[:,0]
# xfin = X0
Time = np.arange(0, Players['T']+Players['delta'], Players['delta']);
L=len(Time) #length of the time horizon

iter = 0
intloop = 0
finloop = RH*Players['delta']
cmode = np.zeros(RHsteps)

for k in range(RHsteps):
#for k in range(8):
    aclcnt = 0
    mode, amap = RHmode(xfin, Active, Players) # RHmode funtion- output mode and amap (look at RHmode function)
    print(amap)
    Acl=np.zeros((L,2*(Active['N']), 2*(Active['N'])))
    #Acl matrix computation
    Acl = RHstep(Active, Players, mode, amap) # RHstep funtion- output Acl (look at RHstepfunction)
   
    cmode[iter] = mode #current iteration mode of the game
    #starting mode of the game
    if iter == 0:
        if cmode[iter] == 0:
            print("\n Game starts in the Rescue mode \n") #rescue mode 
        else:
            print("\n Game starts in the Interception mode \n") #interception mode
            
    if iter > 0:
        if abs(cmode[iter] - cmode[iter-1]) > 0: #swiching mode condition
            if cmode[iter] == 1:
                print("\n Game switches to Interception mode at %3.5f \n" % intloop) #interception mode
                
            else:
                print("\n Game switches to Rescue mode at %3.5f \n" % intloop) #rescue mode
                
    
    if Active['epochflag'] == 1:
        Acl = expandAcl(Acl, Active)

    for m in np.arange(intloop, finloop + Players['delta'], Players['delta']):
         d=expm(Acl[aclcnt, :, :] * Players['delta']) @ x[:, xcnt]  #solution of the closedloop system
         d=d.reshape(-1,1)
         x=np.append(x,d,axis=1)
         xcnt+=1 #increase x count
         aclcnt+=1 #increse Acl acound
         # Game temination check in the following gmterm function
         
         Active = gmterm(x[:, xcnt], Active, Players, mode, m) # more details look at gmterm function
    
         if Active['eventflag'] == 1:
            intloop = m + Players['delta']
            finloop = m + Players['delta'] + RH * Players['delta']
            iter = iter + 1
            break

         if Active['TERMflag'] == 1:
            break
         else:
            xfin = x[:, xcnt]
           

    if Active['eventflag'] == 0:
        intloop = finloop + Players['delta']
        finloop = finloop + RH * Players['delta']
        iter = iter + 1

    if Active['TERMflag'] == 1:
        break
 ############################################### Plotting #########################################   
plotdata(x,Active)
##---------------------------CSV file-------------------------------------##
print("\n Trajectories of the agents are written in the .csv file TrajectoryData.csv")

with open(file1, 'w') as csvfile: #csv file data 
 # creating a csv writer object 
  csvwriter = csv.writer(csvfile) 
  csvwriter.writerow(fields) #header name
    #csvwriter.writerows(rows) #rows name for each player
  csvwriter.writerows(x.T) #state data in each row 
    
    




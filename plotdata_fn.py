##This Pythhon code is used for plotting the state trajectories
#Author- Aniruddha Roy, Department of Electrical Engineering, mail-ee18d031@smail.iitm.ac.in 
#Python library
import matplotlib.pyplot as plt
l=0.02

def plotdata(x, Active):
    # 2A-2D-1T
    if Active['maxN']==5:
        plt.plot(x[0,:], x[1,:], 'r', x[2,:], x[3,:], 'r', x[4,:], x[5,:], 'b', 
                 x[6,:], x[7,:], 'b', x[8,:], x[9,:], 'k', linewidth=1.5)
        plt.text(x[0,0]+l,x[1,0]+l,'$a_{0}$',None,fontsize = 14) #attacker-0
        plt.text(x[2,0]+l,x[3,0]+l,'$a_{1}$',None,fontsize = 14) #attacker-1
        plt.text(x[4,0]+l,x[5,0]+l,'$d_{0}$',None,fontsize = 14) #defender-0
        plt.text(x[6,0]+l,x[7,0]+l,'$d_{1}$',None,fontsize = 14) #defender-1
        plt.text(x[8,0]+l,x[9,0]+l,'$t$',None,fontsize = 14) #target
       
    if Active['maxN']==6:
        if Active['maxNa'] > Active['maxNd']: #3A-2D-1T
            plt.plot(x[0,:], x[1,:], 'r', x[2,:], x[3,:], 'r', x[4,:], x[5,:], 'r', 
                     x[6,:], x[7,:], 'b', x[8,:], x[9,:], 'b', x[10,:], x[11,:],'k', linewidth=1.5)
            plt.text(x[0,0]+l,x[1,0]+l,'$a_{0}$',None,fontsize = 14) #attacker-0
            plt.text(x[2,0]+l,x[3,0]+l,'$a_{1}$',None,fontsize = 14) #attacker-1
            plt.text(x[4,0]+l,x[5,0]+l,'$a_{2}$',None,fontsize = 14) #attacker-2
            plt.text(x[6,0]+l,x[7,0]+l,'$d_{0}$',None,fontsize = 14) #defender-0
            plt.text(x[8,0]+l,x[9,0]+l,'$d_{1}$',None,fontsize = 14) # defender-1
            plt.text(x[10,0]+l,x[11,0]+l,'$t$',None,fontsize = 14) # target
            
        if Active['maxNa'] < Active['maxNd']: #2A-3D-1T
            plt.plot(x[0,:], x[1,:], 'r', x[2,:], x[3,:], 'r', x[4,:], x[5,:], 'b', 
                     x[6,:], x[7,:], 'b', x[8,:], x[9,:], 'b', x[10,:], x[11,:],'k', linewidth=1.5)
            plt.text(x[0,0]+l,x[1,0]+l,'$a_{0}$',None,fontsize = 14) #attacker-0
            plt.text(x[2,0]+l,x[3,0]+l,'$a_{1}$',None,fontsize = 14) #attacker-1
            plt.text(x[4,0]+l,x[5,0]+l,'$d_{0}$',None,fontsize = 14) #defender-0
            plt.text(x[6,0]+l,x[7,0]+l,'$d_{1}$',None,fontsize = 14) #defender-1
            plt.text(x[8,0]+l,x[9,0]+l,'$d_{2}$',None,fontsize = 14) #defender-2
            plt.text(x[10,0]+l,x[11,0]+l,'$t$',None,fontsize = 14) # target
        
        
    if Active['maxN'] == 7: #3A-3D-1T
        plt.plot(x[0,:], x[1,:], 'r', x[2,:], x[3,:], 'r', x[4,:], x[5,:], 'r', 
                 x[6,:], x[7,:], 'b', x[8,:], x[9,:], 'b', x[10,:], x[11,:], 'b', x[12,:], x[13,:], 'k', linewidth=1.5)
        plt.text(x[0,0]+l,x[1,0]+l,'$a_{0}$',None,fontsize = 14) #attacker-0
        plt.text(x[2,0]+l,x[3,0]+l,'$a_{1}$',None,fontsize = 14) #attacker-1
        plt.text(x[4,0]+l,x[5,0]+l,'$a_{2}$',None,fontsize = 14) #attacker-2
        plt.text(x[6,0]+l,x[7,0]+l,'$d_{0}$',None,fontsize = 14) #defender-0
        plt.text(x[8,0]+l,x[9,0]+l,'$d_{1}$',None,fontsize = 14) # defender-1
        plt.text(x[10,0]+l,x[11,0]+l,'$d_{2}$',None,fontsize = 14) # defender-2
        plt.text(x[12,0]+l,x[13,0]+l,'$t$',None,fontsize = 14) # target
        
    if Active['maxN'] == 8:
        if Active['maxNa'] > Active['maxNd']: #4A-3D-1T
            plt.plot(x[0,:], x[1,:], 'r', x[2,:], x[3,:], 'r', x[4,:], x[5,:], 'r', 
                 x[6,:], x[7,:], 'r', x[8,:], x[9,:], 'b', x[10,:], x[11,:], 'b', x[12,:], x[13,:], 'b', x[14,:], x[15,:], 'k', linewidth=1.5)
            plt.text(x[0,0]+l,x[1,0]+l,'$a_{0}$',None,fontsize = 14) #attacker-0
            plt.text(x[2,0]+l,x[3,0]+l,'$a_{1}$',None,fontsize = 14) #attacker-1
            plt.text(x[4,0]+l,x[5,0]+l,'$a_{2}$',None,fontsize = 14) #attacker-2
            plt.text(x[6,0]+l,x[7,0]+l,'$a_{3}$',None,fontsize = 14) #attacket-3
            plt.text(x[8,0]+l,x[9,0]+l,'$d_{0}$',None,fontsize = 14) # defender-0
            plt.text(x[10,0]+l,x[11,0]+l,'$d_{1}$',None,fontsize = 14) # defender-1
            plt.text(x[12,0]+l,x[13,0]+l,'$d_{2}$',None,fontsize = 14) # defender-2
            plt.text(x[14,0]+l,x[15,0]+l,'$t$',None,fontsize = 14) # target
            
        if Active['maxNa'] < Active['maxNd']: #3A-4D-1T
            plt.plot(x[0,:], x[1,:], 'r', x[2,:], x[3,:], 'r', x[4,:], x[5,:], 'r', 
                 x[6,:], x[7,:], 'b', x[8,:], x[9,:], 'b', x[10,:], x[11,:], 'b', x[12,:], x[13,:], 'b', x[14,:], x[15,:], 'k', linewidth=1.5)
            plt.text(x[0,0]+l,x[1,0]+l,'$a_{0}$',None,fontsize = 14) #attacker-0
            plt.text(x[2,0]+l,x[3,0]+l,'$a_{1}$',None,fontsize = 14) #attacker-1
            plt.text(x[4,0]+l,x[5,0]+l,'$a_{2}$',None,fontsize = 14) #attacker-2
            plt.text(x[6,0]+l,x[7,0]+l,'$d_{0}$',None,fontsize = 14) #defender-0
            plt.text(x[8,0]+l,x[9,0]+l,'$d_{1}$',None,fontsize = 14) # defender-1
            plt.text(x[10,0]+l,x[11,0]+l,'$d_{2}$',None,fontsize = 14) # defender-2
            plt.text(x[12,0]+l,x[13,0]+l,'$d_{3}$',None,fontsize = 14) # defender-3
            plt.text(x[14,0]+l,x[15,0]+l,'$t$',None,fontsize = 14) # target 
            
    if Active['maxN'] == 9:
        plt.plot(x[0,:], x[1,:], 'r', x[2,:], x[3,:], 'r', x[4,:], x[5,:], 'r', 
                 x[6,:], x[7,:], 'r', x[8,:], x[9,:], 'b', x[10,:], x[11,:], 'b', x[12,:], x[13,:], 'b', x[14,:], x[15,:], 'b', x[16,:], x[17,:], 'k', linewidth=1.5)


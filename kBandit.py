#Run cell
# %%
###Import necessary libraries
import random as rd
import numpy as np
import matplotlib.pyplot as plt


###Define a random number in the interval [0,1] to simulate results of
###probabilistic experiments.
'''
This function will throw a random number between 0 and 1. If the result of the random number is lower than the number we defined, 
the function will return true, and it will return false otherwise.
'''
def decision(probability):
    return rd.random() < probability

'''
The second function is the ε-greedy algorithm which will decide on which machine to play.
It can be the machine with highest expected value or a random one.
'''
### Choose which machine to play following the E-greedy method.
def greedy(no_machines,probability):
    aux=decision(probability)
    if(aux==True):
        index=rd.randint(0,len(no_machines)-1)

    else:
        index=np.argmax(no_machines)
    return index

### This variable holds the real probability of winning that each machine has.
### This variable is unknown to the player and it is what we'll try to estimate. 
prob_win=[.8,.85,.9,.7]
### We will try different epsilons to see which one is better. 1 - epilson: .05 mean 5% exploration,95 exploitation
epsilon=[0,.05,.1,.15,.2,.25,.3,.35,.4,.45,.5]
###Variables that hold the total for each different simulation(E=(0,.1,.2,...).
p_total_reward=[]
p_chosen_machine=[]

'''
The first loop will be used to go through all ε=[0,.05,.1,.15,.2,.25,.3,.35,.4,.45,.5].
The second loop for all 10,000 cycles in each gameplay.
The third cycle for the 1000 times played.
'''
for j in range(len(epsilon)):
    ### Here the evolution of the algorithm can be seen. This variable shows
    ### the evolution of the average prize. With the average prize the performance
    ### of the algorithm is shown.
    average_prize=[]
    ###Variable that holds the total prize for each iteration.
    total_reward_acum_g=[]
    ###At the end of each cycle we will choose the machine that has the highest
    ###expected prize and save it in this variable.
    chosen_machine_g=[]
    for x in range(10000):
        ###The algorithm will be tested many times to see it's performance
        ### variable that indicates the prize by playing 1000 times.
        total_reward=0
        ### Number of times played
        i=0
        ### Númber of times played over each machine.
        iteraciones_por_accion=[0,0,0,0]
        ### The expected prize over each machine. The value is started at 10
        ### so that initially all machines are tested.
        expected_prize_action=[10,10,10,10]
        for x in range(100):
          ###Index is the machine that was chosen to play with
          index=greedy(expected_prize_action,epsilon[j])
          ###Esta parte emula si ganaste o perdiste   
          res=decision(prob_win[index])
          if (res==True):
              g=2
          else:
              g=1
          ###Total reward   
          total_reward=total_reward+g
          i=i+1 
          #Total average prize
          average_prize.append(total_reward/i)
          ###Number of times played per machine.
          iteraciones_por_accion[index]=iteraciones_por_accion[index]+1
          ###Update the value of the expected prize
          expected_prize_action[index]=(expected_prize_action[index])+(1/iteraciones_por_accion[index])*(g-expected_prize_action[index])
        ###results after playing 1000 times
        total_reward_acum_g.append(total_reward)
        chosen_machine_g.append(np.argmax(expected_prize_action))
    print(epsilon[j])
    print("On average "+str(sum(total_reward_acum_g)/len(total_reward_acum_g))+" points were obtained.")
    print("The machine was chosen correctly " +str(chosen_machine_g.count(np.argmax(prob_win)))+" times.")
    p_total_reward.append(sum(total_reward_acum_g)/len(total_reward_acum_g))
    p_chosen_machine.append(chosen_machine_g.count(np.argmax(prob_win)))

values=p_total_reward
values2=p_chosen_machine
eje_x=epsilon
eje_x[-1]
fig, ax = plt.subplots(figsize=(20, 14)) 
plt.xticks(rotation=90)
plt.plot(eje_x,values , marker ="o",label = "Average Total Prize");

ylabels = ['{:,}'.format(int(x)) + "K" for x in ax.get_yticks()*(1/1000)]
plt.legend(prop={'size': 24})
plt.title("Figure 1", fontdict=None, loc='center', pad=None,fontsize=18)
plt.xlabel("Epsilon", fontdict=None, labelpad=None,fontsize=18)
# %%

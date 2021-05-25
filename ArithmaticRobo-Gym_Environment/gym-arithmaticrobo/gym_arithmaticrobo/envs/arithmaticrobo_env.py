import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym import spaces
import numpy as np
import random

class ArithmaticRobo(gym.Env):

    metadata = {'render.modes': ['human', 'rgb_array','ansi']}
    
    def __init__(self):
        print("In init")
        
        #self.state = np.array([0,0],dtype=np.float64)
        self.state = np.zeros((1, 2))
        #print(self.state)
        self.x = random.randint(50, 200)
        self.y = random.randint(40, 250)
        self.done = 0
        self.reward=0.0
        self.action_space = spaces.Discrete(4)    


    def step(self, target):
        
        # ADD Action
        if(target==0):
            print("In ADD")
            print(self.x, self.y)
            if(self.x == self.y):
                print("Game Over")                
                self.done = 1
            else: 
                # if y is more than x , to increment x is the right action, so reward of 2.
                # if y is less than x , then increment x is not the correct action , so reward of -1
                if(self.y > self.x):
                    print('In ADD Reward') 
                    print(self.x, self.y)
                    self.x+=1
                    self.reward=2
                else:
                    print("add none")
                    self.reward = -1
        
        # SUBTRACT Action
        if(target==1):            
            print("In SUBTRACT")
            print(self.x, self.y)
            if(self.x == self.y):
                print("Game Over")                
                self.done = 1                
            else:
                # if x is more than y , to decrement x is the right action, so reward of 2.
                # if x is less than y , then increment x is not the correct action , so reward of -1
                if(self.x > self.y):
                    print('In SUBTRACT Reward') # this is the right SUBTRACT scenario (x > y and modulo not satisfied)
                    print(self.x, self.y)
                    self.x-=1
                    self.reward = 2
                else:
                    print("subtract none")
                    self.reward = -1
        
        # DIV Action
        if(target==2):
            print("In Divide")
            print(self.x,self.y)
            if(self.x == self.y):
                print("Game Over")                
                self.done = 1                
            else:
                # if x is more than y by mul factor of one or more then to divide x is the right action, so reward of 5.
                # else reward of -1
                mul_fac_div = self.x/self.y
                print(mul_fac_div)
                if(mul_fac_div >= 1):
                    print("In DIVIDE Reward")
                    print(self.x, self.y)
                    self.x = int(round((self.x//mul_fac_div),2))
                    self.reward = 5
                else:
                    print("div none") 
                    self.reward = -1
        
        # MULTIPLY Action
        if(target==3): 
            print("In Multiply")
            print(self.x,self.y)
            if(self.x == self.y):
                print("Game Over")                
                self.done = 1                
            else:
                # if y is more than x by mul factor of one or more then to multiply x is the right action, so reward of 5.
                # else reward of -1
                mul_fac_mult= self.y/self.x
                print(mul_fac_mult)
                if(mul_fac_mult >= 1):
                    print("In MULTIPLY Reward")
                    print(self.x, self.y)
                    self.x = int(round((self.x * mul_fac_mult),2))
                    self.reward = 5
                else:
                    print("mul none")
                    self.reward = -1
        
        self.state[0,0]=self.x
        self.state[0,1]=self.y
        return np.copy(self.state.flatten()), self.reward, self.done, {}

    def reset(self):
        print("In Reset")
        self.state = np.zeros((1, 2))
        self.x = random.randint(50, 200)
        self.y = random.randint(40, 250)
        self.done = 0
        self.reward =0
        return np.copy(self.state.flatten())

    def render(self):
        if mode == 'human':
            print("In Render")
            print(self.x, "---" , self.y)
        
                

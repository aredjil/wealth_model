#!/usr/bin/env python3

import mesa 

import seaborn as sns 

import numpy as np 

import pandas as pd 


class Money_agent(mesa.Agent):
    """
    Agent class 
    """
    def __init__(self, model):
        super().__init__(model)
        self.wealth = self.random.randint(1, 10) # Intial wealth of each agent 
    #NOTE: Add randomly intilized wealth, an agent can be intilized with 100-1 randomly  
    def exchange(self):
        if self.wealth > 0:
            other_agent = self.random.choice(self.model.agents) # randomly choose an agent to trade with 
            if other_agent is not None:
                other_agent.wealth += 1 # increase the wealth of the chosen agent by 1 
                self.wealth -= 1 # decrease your welath by 1 
 
class Money_model(mesa.Model):
    """
    Model class that defines the dynamics of agents. 
    """
    def __init__(self, n, seed=None, ):
        super().__init__(seed=seed)
        assert isinstance(n, int), "The number of agents n must be an interger"
        self.num_agents = n
        for _ in range(self.num_agents):
            a = Money_agent(self)
    def step(self):
        # print("Hello world")
        self.agents.shuffle_do("exchange")
                

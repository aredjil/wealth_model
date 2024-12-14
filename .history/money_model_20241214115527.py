#!/usr/bin/env python3

import mesa 

import seaborn as sns 

import numpy as np 

import pandas as pd 


class Money_agent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1
    def exchange(self):
        if self.wealth > 0:
            other_agent = self.random.choice(self.model.agents)
            if other_agent is not None:
                other_agent.wealth += 1
                self.wealth -= 1 
 
class Money_model_random_exchange(mesa.Model):
    """
    This class defines a model where agents exchange wealth with a randomly selected agent
    """
    def __init__(self, n, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        for _ in range(self.num_agents):
            a = Money_agent(self)
    def step(self):
        # print("Hello world")
        self.agents.shuffle_do("exchange")

class Money_model_spatial_exchange(mesa.model):
    def __init__(self, n, width, hight, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n 



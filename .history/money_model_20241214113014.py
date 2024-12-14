#!/usr/bin/env python3

import mesa 

import seaborn as sns 

import numpy as np 

import pandas as pd 


class Money_agent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1
    def say_hi(self):
        print(f"Hi, I am an agent, you can call me {str(self.unique_id)}.")
    def say_wealth(self):
        print(f"Hye I am agent {str(self.unique_id)} my wealth is {int(self.wealth)}")

class Money_model(mesa.Model):
    def __init__(self, n, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        for _ in range(self.num_agents):
            a = Money_agent(self)
    def step(self):
        # print("Hello world")
        self.agents.shuffle_do("say_waelth")


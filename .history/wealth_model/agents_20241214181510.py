#!/usr/bin/env python3

import mesa 

"""
Agent class definition
"""
class Money_agent(mesa.Agent):
    """
    Agent class 
    """
    def __init__(self, model, random=False):
        super().__init__(model)
        self.wealth = self.random.randint(1, 10) if random else  1
    #NOTE: Add randomly intilized wealth, an agent can be intilized with 100-1 randomly  
    def exchange(self):
        if self.wealth > 0:
            other_agent = self.random.choice([a for a in self.model.agents if a != self]) # randomly choose an agent to trade with 
            if other_agent is not None:
                other_agent.wealth += 1 # increase the wealth of the chosen agent by 1 
                self.wealth -= 1 # decrease your welath by 1 
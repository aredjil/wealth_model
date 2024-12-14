#!/usr/bin/env python3

import mesa 

from wealth_model.agents import  
"""
Compute Gini coefficient 
"""
def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.agents]
    x = sorted(agent_wealths)
    n = model.num_agents
    B = sum(xi * (n - i) for i, xi in enumerate(x)) / (n * sum(x))
    return 1 + (1 / n) - 2 * B

class Money_model(mesa.Model):
    """
    Model class that defines the dynamics of agents. 
    """
    def __init__(self, n, seed=None, random=False):
        super().__init__(seed=seed)
        assert isinstance(n, int), "The number of agents n must be an interger"
        self.num_agents = n 
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        )
        for _ in range(self.num_agents):
            a = Money_agent(self, random)
    def step(self):
        # print("Hello world")
        self.datacollector.collect(self)
        self.agents.shuffle_do("exchange")
                
if __name__ == "__main__":
    print("Model class")
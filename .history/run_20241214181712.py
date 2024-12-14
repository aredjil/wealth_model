#!/usr/bin/env python3

from wealth_model.money_model import Money_model 
import seaborn as sns 
from matplotlib import pyplot as plt 
from tqdm import tqdm 
import sys 
"""
Script to run the model 
"""
def main():
    print(""" 
    Usage:
        python main.py <#agents> <#iterations>
    Default: 
          python main.py 10 10   
""")
    n_agents = 10
    n_iter = 100
    if len(sys.argv) > 1:
        n_agents = int(sys.argv[1])
    if len(sys.argv) > 2:
        n_iter = int(sys.argv[2])
    print(f"Running the simulation for: {n_agents} agents, and {n_iter} iterations\n")
    model = Money_model(n_agents)
    for _ in tqdm(range(n_iter)):
        model.step()
    gini = model.datacollector.get_model_vars_dataframe()
    wealth = model.datacollector.get_agent_vars_dataframe()
    g1 = sns.lineplot(data=gini)
    g2 = sns.histplot(data=wealth, discrete=True)
    plt.show()


if __name__ == "__main__":
    main()

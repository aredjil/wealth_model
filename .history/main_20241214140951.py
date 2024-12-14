#!/usr/bin/env python3
from models.money_model import Money_model 
import seaborn as sns 
from matplotlib import pyplot as plt 
from tqdm import tqdm 
import sys 

def main():
    if len(sys.argv) > 1:
        n_agents = int(sys.argv[1])
    elif len(sys.argv) > 2:
        n_models = int(sys.argv[2])
    elif len(sys.argv) > 3:
        n_iter = int(sys.argv[3])
    else:
        n_agents = 10
        n_iter = 10
        n_models = 1
    all_wealth = []
    model = Money_model(n_agents)
    print(f"Running the simulation for: {n_agents} agents, {n_models} models, and {n_iter} iterations")
    for _ in tqdm(range(n_models)):
        model = Money_model(n_agents)
        for _ in range(n_iter):
            model.step()
        for agent in model.agents:
            all_wealth.append(agent.wealth) #normlized wealth 
    g = sns.histplot(all_wealth, discrete=True)
    g.set(title=f"Wealth Distrubution after {n_iter} iterations", xlabel="Wealth", ylabel="number of agents")
    # plt.xticks([tick for tick in range(n_agents)])
    plt.show()
if __name__ == "__main__":
    print(""" 
    Usage:
        python main.py <#agents> <#iterations> <#models>
    Default: 
          python main.py 10 10 1   
""")
    main()
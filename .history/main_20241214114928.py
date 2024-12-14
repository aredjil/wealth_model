#!/usr/bin/env python3
from money_model import Money_model 
import seaborn as sns 
from matplotlib import pyplot as plt 
from tqdm import tqdm 
def main():
    n_agents = 100 
    n_iter = 10
    n_models = 100
    all_wealth = []
    print(f"Running the simulation for {}")
    for _ in tqdm(range(n_models)):
        model = Money_model(n_agents)
        for _ in range(n_iter):
            model.step()
        for agent in model.agents:
            all_wealth.append(agent.wealth) #normlized wealth 
    g = sns.histplot(all_wealth, discrete=True)
    g.set(title=f"Wealth Distrubution after {n_iter} iterations", xlabel="Wealth", ylabel="number of agents")
    plt.show()
if __name__ == "__main__":
    main()
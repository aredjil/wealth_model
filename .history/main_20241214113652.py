#!/usr/bin/env python3
from money_model import Money_model 
import seaborn as sns 
from matplotlib import pyplot as plt 
def main():
    n_agents = 10 
    n_iter = 100
    my_model = Money_model(n_agents)
    for _ in range(n_iter):
        my_model.step()
    agent_wealth = [a.wealth for a in my_model.agents]
    g = sns.histplot(agent_wealth, discrete=True)
    g.set(title=f"Wealth Distrubution after 20 iterations", xlabel="Wealth", ylabel="number of agents")
    plt.show()
if __name__ == "__main__":
    main()
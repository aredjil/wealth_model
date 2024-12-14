#!/usr/bin/env python3
from money_model import Money_model 
import seaborn as sns 
from matplotlib import pyplot as plt 
def main():
    n_agents = 10 
    n_iter = 30
    

    g = sns.histplot(agent_wealth, discrete=True)
    g.set(title=f"Wealth Distrubution after {n_iter} iterations", xlabel="Wealth", ylabel="number of agents")
    plt.show()
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
from mesa.visualization import SolaraViz, make_plot_component, make_space_component
import mesa 

from models.money_model import Money_model 
import seaborn as sns 
from matplotlib import pyplot as plt 
from tqdm import tqdm 
import sys 

# To decrease the effect of the noise consider running several models 
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
    model = Money_model(n_agents)
    print(f"Running the simulation for: {n_agents} agents, and {n_iter} iterations\n")
    for _ in tqdm(range(n_iter)):
        model.step()
    gini = model.datacollector.get_agent_vars_dataframe()
    # print(gini.head())
    # g.set_title(title="Gini Coefficient over time", ylabel="Gini Coefficient")  
    # g = sns.histplot(all_wealth, discrete=True, color="#2ca25f")
    # g.set(title=f"Wealth Distrubution after {n_iter} iterations", xlabel="Wealth", ylabel="number of agents")
    plt.show()
if __name__ == "__main__":
    main()
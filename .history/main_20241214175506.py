#!/usr/bin/env python3
from mesa.visualization import SolaraViz, make_plot_component, make_space_component
import mesa 

from models.money_model import Money_model 
import seaborn as sns 
from matplotlib import pyplot as plt 
from tqdm import tqdm 
import sys 

def dashboard():
    model_params = {
    "n": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of agents:",
        "min": 10,
        "max": 100,
        "step": 1,
    }
    }
    model
# To decrease the effect of the noise consider running several models 
def main():
    print(""" 
    Usage:
        python main.py <#agents> <#iterations>
    Default: 
          python main.py 10 10   
""")
    n_agents = 20
    n_iter = 1000
    if len(sys.argv) > 1:
        n_agents = int(sys.argv[1])
    if len(sys.argv) > 2:
        n_iter = int(sys.argv[2])
    print(f"Running the simulation for: {n_agents} agents, and {n_iter} iterations\n")
    model = Money_model(n_agents)
    for _ in tqdm(range(n_iter)):
        model.step()
    gini = model.datacollector.get_model_vars_dataframe()
    g = sns.lineplot(data=gini)
    # gini.reset_index(inplace=True)
    # g = sns.lineplot(data=gini)
    # g = sns.histplot(all_wealth, discrete=True, color="#2ca25f")
    # g.set(title=f"Wealth Distrubution after {n_iter} iterations", xlabel="Wealth", ylabel="number of agents")
    plt.show()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
from mesa.visualization import SolaraViz, make_plot_component, make_space_component
import mesa 

from models.money_model import Money_model 
import seaborn as sns 
from matplotlib import pyplot as plt 
from tqdm import tqdm 
import sys 

# To decrease the effect of the noise consider running several models 
# def main():
#     print(""" 
#     Usage:
#         python main.py <#agents> <#iterations>
#     Default: 
#           python main.py 10 10   
# """)
#     n_agents = 100
#     n_iter = 100
#     if len(sys.argv) > 1:
#         n_agents = int(sys.argv[1])
#     if len(sys.argv) > 2:
#         n_iter = int(sys.argv[2])
#     print(f"Running the simulation for: {n_agents} agents, and {n_iter} iterations\n")
#     model = Money_model(n_agents)
#     for _ in tqdm(range(n_iter)):
#         model.step()
#     gini = model.datacollector.get_agent_vars_dataframe()
#     print(gini.index)
#     # g = sns.lineplot(data=gini, x=gini.index, y="Gini")
#     # gini.reset_index(inplace=True)
#     # g = sns.lineplot(data=gini)
#     # g = sns.histplot(all_wealth, discrete=True, color="#2ca25f")
#     # g.set(title=f"Wealth Distrubution after {n_iter} iterations", xlabel="Wealth", ylabel="number of agents")
#     plt.show()
def main():
    n_agents = 10
    n_iter = 100
    if len(sys.argv) > 1:
        n_agents = int(sys.argv[1])
    if len(sys.argv) > 2:
        n_iter = int(sys.argv[2])
    
    model = Money_model(n_agents)
    print(f"Running the simulation for: {n_agents} agents, and {n_iter} iterations\n")

    # Run the simulation
    for _ in range(n_iter):
        model.step()

    # Access and visualize the Gini index
    gini_df = model.datacollector.get_model_vars_dataframe()
    print("Gini Index DataFrame:")
    print(gini_df.head())  # Display first few rows of the Gini DataFrame
    
    # Plot the Gini inde
    sns.lineplot(data=gini_df, x=gini_df.index, y="Gini")
    plt.title("Gini Index Over Time")
    plt.xlabel("Steps")
    plt.ylabel("Gini Index")
    plt.show()

    # Access and visualize agent-level wealth data
    agent_df = model.datacollector.get_agent_vars_dataframe()
    print("Agent Wealth DataFrame:")
    print(agent_df.head())  # Display first few rows of the agent DataFrame
    
    # Optional: Visualize wealth distribution
    wealth_data = agent_df.reset_index()  # Reset index to plot wealth vs. step
    sns.lineplot(data=wealth_data, x="Step", y="Wealth", hue="AgentID", legend=False)
    plt.title("Agent Wealth Over Time")
    plt.xlabel("Steps")
    plt.ylabel("Wealth")
    plt.show()

if __name__ == "__main__":
    main()
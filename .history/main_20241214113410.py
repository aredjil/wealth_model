#!/usr/bin/env python3
from money_model import Money_model 



def main():
    n = 10 
    my_model = Money_model(n)
    for _ in range(20):
        my_model.step()
    agent_wealth = []
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
from money_model import Money_model 



def main():
    n = 10 
    my_model = Money_model(n)
    my_model.step()
if __name__ == "__main__":
    main()
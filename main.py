# World population analyst

#Imports
from population_functions import ask_country_name,try_again,choice1,choice2,choice3

#run function
def run():
    #UI
    choice=input(""" Welcome to your world population analyst, what do you want to discover today:
                 1. A country population 
                 2. A country capital
                 3. Total world population (2022)
                 
                 =""")
    
    #Choice1
    if choice=="1":
        country_name=ask_country_name()
        choice1(country_name)

    #Choice2
    elif choice=="2":
        country_name=ask_country_name()
        choice2(country_name)
    
    #Choice3
    elif choice=="3": choice3()
        
    else:
        r=try_again()
        if r=="restart": run()

if __name__=="__main__":
    run()
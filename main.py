# World population analysis

#Imports
from population_functions import converts_csv_to_list,ask_country_name,try_again

#def function
def run():
    header,countries=converts_csv_to_list()
    
    #UI
    choice=input(""" Welcome to your world population analyst, what do you want to discover today:
                 1. A country population 
                 2. A country capital
                 3.
                 4.
                 5.
                 
                 =""")
    
    # Here we create a dict per country, this will be useful later on
    countries_dicts=[dict(zip(header,country)) for country in countries]
    
    #Choice1
    if choice=="1":
        country_name=ask_country_name()
        result=[d["2022 Population"] for d in countries_dicts if d["Country/Territory"]==country_name][0]
        print("The population of",country_name,"is",str(result),"people")
        
    #Choice2
    elif choice=="2":
        country_name=ask_country_name()
        result=[d["Capital"] for d in countries_dicts if d["Country/Territory"]==country_name][0]
        print("The capital of",country_name,"is",str(result))
        
    else:
        try_again()  

if __name__=="__main__":
    run()
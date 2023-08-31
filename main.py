# World population analysis

from data_cleaning import converts_csv_to_list

def ask_country_name():
    country_name=input("What's your country name? ").capitalize()
    return country_name

def run():
    header,countries=converts_csv_to_list()
    
    #UI
    choice=input(""" Welcome to this world population analyst, what do you want to discover today:
                 1. My country's population 
                 2. 
                 3.
                 4.
                 5.
                 
                 :""")
    
    # Here we create a dict per country, this will be useful later on
    countries_dicts=[dict(zip(header,country)) for country in countries]
    
    #Choice 1
    if choice=="1":
        country_name=ask_country_name()
        result=[d["2022 Population"] for d in countries_dicts if d["Country/Territory"]==country_name][0]
        print("Your country population is",str(result),"people")

if __name__=="__main__":
    run()
# Population functions

#Imports
import csv
from functools import reduce
import pandas as pd

# Functions
    
def ask_country_name():
    country_name=input("What's your country name? ").capitalize()
    return country_name

def try_again(missing="Option"):
    error_menu=input(missing+""" not found, 
    Press 1 to try again
    Press 2 to close this program
    =""")
    if error_menu=="1":
        return "restart"
    elif error_menu=="2":
        exit()
    else:
        try_again()

def choice1(country_name):
    try:
        result=[d["2022 Population"] for d in countries_dicts if d["Country/Territory"]==country_name][0]
        print("The population of",country_name,"is",str(result),"people")
    except IndexError:
        try_again('Country')
        
def choice2(country_name):
    try:
        result=[d["Capital"] for d in countries_dicts if d["Country/Territory"]==country_name][0]
        print("The capital of",country_name,"is",str(result))
    except IndexError:
        try_again('Country')
        
def choice3():
    populations_2022=[int(l[5]) for l in countries]
    total_world_population=reduce(lambda x,y:x+y,populations_2022)
    print("The total world population in 2022 is",str(total_world_population),"people")

# Data manipulation
with open("./world_population.csv") as csvfile:
    reader=csv.reader(csvfile)
    header=next(reader)
    countries=list(reader)

# Here we create a dict per country, this will be useful later on
countries_dicts=[dict(zip(header,country)) for country in countries]

# Creating a pandas Series object from the before used data
countries_series=pd.Series(countries_dicts,index=[d["Country/Territory"] for d in countries_dicts],name="Countries population data")

# Creating a pandas DataFrame
df=pd.DataFrame(countries_dicts)
print(df)
        
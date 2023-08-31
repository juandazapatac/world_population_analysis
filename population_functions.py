# Population functions

import csv

def converts_csv_to_list():
    with open("./world_population.csv") as csvfile:
        reader=csv.reader(csvfile)
        header=next(reader)
        countries=list(reader)
        return (header,countries)
    
def ask_country_name():
    country_name=input("What's your country name? ").capitalize()
    return country_name

def try_again():
    choice2=input("""Option not found, 
    Press 1 to try again
    Press 2 to close this program
    =""")
    if choice2=='1':
        run()
    elif choice2=='2':
        exit()
    else:
        try_again()
    
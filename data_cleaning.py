# Data cleaning

import csv

def converts_csv_to_list():
    with open("./world_population.csv") as csvfile:
        reader=csv.reader(csvfile)
        header=next(reader)
        countries=list(reader)
        return (header,countries)
    
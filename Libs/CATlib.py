import csv
from . import GRBlib

# TODO Update the program to read all kinds of catalogues in csv comma separated files and identify the columns
# Reflection: is it possible to write a data-agnostic catalogue class? 

def BATSE_catalog(filename):
    # This assumes the catalogue is a csv file comma separated with:
    # position 0 : GRB name
    # position 1 : T90
    # position 2 : Fluence
    # position 3 : Flux
    CATALOG = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                newMember = GRBlib.GRB(name = row[0], fluence= float(row[2]), T90=float(row[1]), flux = float(row[3]))
                CATALOG.append(newMember)
                line_count += 1
    return CATALOG
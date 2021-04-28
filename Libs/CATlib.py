import csv
import GRBlib

def BATSE_catalog(filename):
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
import csv
import os

from machine import Machine

def load_machine_data(csv_path):
    """Returns a list of Machines based on the csv file

    Keyword Arguements:
    - csv_path: the path on the machine that leads to the data
    """
    machines = []
    with open(csv_path, 'r') as csvfile:
        # Open the machine data and load each machine into the machines list
        data = csv.reader(csvfile, delimiter=',')
        next(data, None) # Skip the header line
        for row in data:
            machines.append(Machine(row[0], row[1], row[2], 
                                    row[3], row[4], row[5]))
    return machines

"""
BEGIN MAIN FILE
"""

WORKING_DIR = os.path.dirname(__file__)

if __name__ == "__main__":
    data_sheet = os.path.join(WORKING_DIR, "data/test_sheet.csv")
    machines = load_machine_data(data_sheet)

    # TODO manipulate machines
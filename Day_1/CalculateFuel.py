import csv

class FuelCalculator:

    def __init__(self):
        self.data = []

    def import_data(self):
       with open('module_masses.csv') as datafile:
        data = csv.reader(datafile, delimiter='/n')
        for mass in data:
            self.data.append(data)
        print(self.data)

test = FuelCalculator()
test.import_data()
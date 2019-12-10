import csv

class FuelCalculator:

    def __init__(self):
        self.data = []

    def import_data(self):
       with open('/home/fvarnals/Projects/Advent_of_Code_2019/Day_1/module_masses.csv') as datafile:
        mass_data = csv.reader(datafile, delimiter='\n')
        for mass in mass_data:
            self.data.append(int(mass[0]))


test = FuelCalculator()
test.import_data()
print test.data
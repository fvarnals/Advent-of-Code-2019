import csv

class FuelCalculator:

    def __init__(self):
        self.masses = []
        self.fuel_requirements = []

    def import_data(self):
       with open('/home/fvarnals/Projects/Advent_of_Code_2019/Day_1/module_masses.csv') as datafile:
        mass_data = csv.reader(datafile, delimiter='\n')
        for mass in mass_data:
            self.masses.append(int(mass[0]))
    
    def fuel_required(self, mass):
        fuel_required = int(mass/3) - 2
        return fuel_required

    def calculate_fuel_requirements(self):
        for mass in self.masses:
            self.fuel_requirements.append(self.fuel_required(mass))


test = FuelCalculator()
test.import_data()
test.calculate_fuel_requirements()
print(test.fuel_requirements)
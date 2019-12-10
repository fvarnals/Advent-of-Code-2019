import csv

class FuelCalculator(object):

    def __init__(self):
        self.masses = []
        self.fuel_requirements = []
        self.total_fuel_required = 0
        self.extra_fuel_required = 0

        self.import_data()
        self.calculate_fuel_requirements()
        self.calculate_total_fuel_required()

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
    
    def calculate_extra_fuel(self,fuel_mass):
        extra_fuel_quantities = [fuel_mass]
        while True:
            mass = extra_fuel_quantities[-1]
            extra_fuel = self.fuel_required(mass)
            if extra_fuel <= 0:
                break
            else:
                extra_fuel_quantities.append(extra_fuel)
        return sum(extra_fuel_quantities)
    
    def calculate_total_extra_fuel(self):
        for fuel_mass in self.fuel_requirements:
            extra_fuel_required = self.calculate_extra_fuel(fuel_mass)
            self.extra_fuel_required += extra_fuel_required
        print(self.extra_fuel_required)

    def calculate_total_fuel_required(self):
        self.total_fuel_required = sum(self.fuel_requirements)

test = FuelCalculator()
test.calculate_extra_fuel(654)
test.calculate_total_extra_fuel()
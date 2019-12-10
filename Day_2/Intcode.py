class Intcode:

    def __init__(self):
        self.opcodes = []
    
    def get_opcodes(self):
        with open('/home/fvarnals/Projects/Advent_of_Code_2019/Day_2/opcodes.txt') as opcodes_data:
            for line in opcodes_data:
                self.opcodes = map(int, line.split(','))
    

test = Intcode()
test.get_opcodes()
print(test.opcodes)
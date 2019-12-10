class Intcode:

    def __init__(self):
        self.opcodes = []
    
    def get_opcodes(self):
        with open('/home/fvarnals/Projects/Advent_of_Code_2019/Day_2/opcodes.txt') as opcodes_data:
            for line in opcodes_data:
                self.opcodes = map(int, line.split(','))

    def run(self):
        for i in range(0, len(self.opcodes), 4):
            code = self.opcodes[i]
            first_index = self.opcodes[i + 1]
            second_index = self.opcodes[i + 2]
            target_index = self.opcodes[i + 3]
            if code == 1:
                self.add_numbers(first_index, second_index, target_index)
            elif code == 2:
                self.multiply_numbers(first_index, second_index, target_index)
            elif code == 99:
                break
            else:
                print(i)
                raise Exception('Error, invalid opcode')
    
    def add_numbers(self,first_index, second_index, target_index):

        self.opcodes[target_index] = self.opcodes[first_index] + self.opcodes[second_index]
    
    def multiply_numbers(self, first_index, second_index, target_index):
        
        self.opcodes[target_index] = self.opcodes[first_index] * self.opcodes[second_index]

test = Intcode()
test.get_opcodes()
test.run()
print(test.opcodes)
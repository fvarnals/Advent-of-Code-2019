from Intcode import Intcode

test = Intcode()

for noun in range(1,100):
    for verb in range(1,100):
        test.get_opcodes()
        test.opcodes[1] = noun
        test.opcodes[2] = verb
        test.run()
        if test.opcodes[0] == 19690720:
            print(f"noun = {noun}, verb = {verb}")
            break

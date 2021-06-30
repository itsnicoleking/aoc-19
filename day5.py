import intcode, copy

file = open("./inputs/input_day5.txt", "r")
intcodes = list(map(int, file.read().split(',')))
file.close

# Part 1
comp = intcode.Intcode(copy.deepcopy(intcodes))
print('Part 1:', comp.execute(1))

# Part 2
comp = intcode.Intcode(copy.deepcopy(intcodes))
print('Part 2:', comp.execute(5))

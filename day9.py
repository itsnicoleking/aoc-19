import intcode

file = open("./inputs/input_day9.txt", "r")
intcodes = list(map(int, file.read().split(',')))
file.close

# Part 1
comp = intcode.Intcode(intcodes, [1])
print('Part 1:', comp.execute())

# Part 2
comp = intcode.Intcode(intcodes, [2])
print('Part 2:', comp.execute())

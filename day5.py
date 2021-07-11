import intcode

file = open("./inputs/input_day5.txt", "r")
intcodes = list(map(int, file.read().split(',')))
file.close

# Part 1
# NOTE: day 7 broke only part 1 ...? but it still works for the test data
# test data: 3,0,4,0,99 -> should output the input
comp = intcode.Intcode(intcodes, [1])
print('Part 1:', comp.execute())

# Part 2
comp = intcode.Intcode(intcodes, [5])
print('Part 2:', comp.execute())

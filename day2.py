import intcode, copy

file = open("./inputs/input_day2.txt", "r")
intcodes = list(map(int, file.read().split(',')))
file.close

# Part 1
comp = intcode.Intcode(copy.deepcopy(intcodes))
comp.set(1, 12)
comp.set(2, 2)
print('Part 1:', comp.execute())

# Part 2
def part2exec(intcodes, noun, verb):
  comp = intcode.Intcode(copy.deepcopy(intcodes))
  comp.set(1, noun)
  comp.set(2, verb)
  return comp.execute()

for noun in range(100):
  for verb in range(100):
    if part2exec(intcodes, noun, verb) == 19690720:
      print('Part 2:', 100 * noun + verb)
      break

# Same same but different
# print('Part 2:', next(100 * noun + verb for noun in range(100) for verb in range(100) if part2exec(intcodes, noun, verb) == 19690720))

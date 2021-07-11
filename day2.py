import intcode

file = open("./inputs/input_day2.txt", "r")
intcodes = list(map(int, file.read().split(',')))
file.close

# Part 1
comp = intcode.Intcode(intcodes)
comp.setValue(1, 12)
comp.setValue(2, 2)
comp.execute()
print('Part 1:', comp.getValue(0))

# Part 2
def part2exec(intcodes, noun, verb):
  comp = intcode.Intcode(intcodes)
  comp.setValue(1, noun)
  comp.setValue(2, verb)
  comp.execute()
  return comp.getValue(0)

for noun in range(100):
  for verb in range(100):
    if part2exec(intcodes, noun, verb) == 19690720:
      print('Part 2:', 100 * noun + verb)
      break

# Same same but different
# print('Part 2:', next(100 * noun + verb for noun in range(100) for verb in range(100) if part2exec(intcodes, noun, verb) == 19690720))

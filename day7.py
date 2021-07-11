import intcode, itertools

file = open("./inputs/input_day7.txt", "r")
intcodes = list(map(int, file.read().split(',')))
file.close

# Part 1
pt1 = 0
for phase in itertools.permutations(range(5)):
  comps = [intcode.Intcode(intcodes, [phase[i]]) for i in range(5)]
  outputIsTheNewInput = 0
  for idx, comp in enumerate(comps):
    comp.addInput(outputIsTheNewInput)
    outputIsTheNewInput = comp.execute()
  pt1 = max(pt1, outputIsTheNewInput)
  
print('Part 1:', pt1)

# Part 2
pt2 = 0
for phase in itertools.permutations(range(5, 10)):
  comps = [intcode.Intcode(intcodes, [phase[i]]) for i in range(5)]
  outputIsTheNewInput = 0
  while all(not comp.isHalted() for comp in comps):
    for idx, comp in enumerate(comps):
      comp.addInput(outputIsTheNewInput)
      outputIsTheNewInput = comp.execute()
    if outputIsTheNewInput is not None:
      pt2 = max(pt2, outputIsTheNewInput)

print('Part 2:', pt2)

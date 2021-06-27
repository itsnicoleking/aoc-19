class Intcode:
  def __init__(self, program):
    self.memory = program
    self.halted = False
    self.instr_ptr = 0

  def _getInstruction(self, instruction_code):
    return next(cls for cls in Instruction.__subclasses__() if cls.opcode == instruction_code)

  def _getParameters(self, num_parameters):
    parameters = []
    for i in range(num_parameters):
      address = self.memory[self.instr_ptr+i+1]
      value = self.memory[address]
      parameters.append(Parameter(address, value))
    return parameters

  def execute(self):
    while not self.halted:
      instruction = self._getInstruction(self.memory[self.instr_ptr])
      parameters = self._getParameters(instruction.num_parameters)
      self.instr_ptr = instruction().execute(self, parameters)
    return self.memory[0]

  def get(self, address):
    return self.memory[address]

  def set(self, address, value):
    self.memory[address] = value


# ===== Parameter =====

class Parameter:
  def __init__(self, address, value):
    self.address = address
    self.value = value


# ===== Instruction & Subclasses =====

class Instruction:
  opcode, num_parameters = 0, 0

  def execute(self, intcode, parameters):
    pass

  def next_instr(self, intcode):
    return intcode.instr_ptr + self.num_parameters + 1


class PlusInstruction(Instruction):
  opcode, num_parameters = 1, 3

  def execute(self, intcode, parameters):
    intcode.set(parameters[2].address, (parameters[0].value + parameters[1].value))
    return self.next_instr(intcode)


class MultiplyInstruction(Instruction):
  opcode, num_parameters = 2, 3

  def execute(self, intcode, parameters):
    intcode.set(parameters[2].address, (parameters[0].value * parameters[1].value))
    return self.next_instr(intcode)


class HaltInstruction(Instruction):
  opcode, num_parameters = 99, 0

  def execute(self, intcode, parameters):
    intcode.halted = True
    return None

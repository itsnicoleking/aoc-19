class Intcode:
  def __init__(self, program):
    self.memory = program
    self.halted = False
    self.instrPtr = 0
    self.input = None
    self.output = None

  def _getInstruction(self, instructionCode):
    return next(cls for cls in Instruction.__subclasses__() if cls.opcode == instructionCode)

  def _getParameters(self, numParameters):
    modes = str(self.memory[self.instrPtr]).zfill(5)[:3][::-1] # fill to 5 chars, take first 3, invert order
    parameters = []
    for i in range(numParameters):
      address = self.memory[self.instrPtr+i+1]
      if modes[i] == '1':
        parameters.append(Parameter(address, address))
      else:
        parameters.append(Parameter(address, self.memory[address]))
    return parameters

  def execute(self, input = None):
    self.input = input
    while not self.halted:
      instruction = self._getInstruction(self.memory[self.instrPtr] % 100)
      parameters = self._getParameters(instruction.numParameters)
      self.instrPtr = instruction().execute(self, parameters)
    return self.output

  def getValue(self, address):
    return self.memory[address]

  def setValue(self, address, value):
    self.memory[address] = value
    
  def getInput(self):
    return self.input
  
  def setOutput(self, output):
    self.output = output
    
  def setHalted(self, haltBool):
    self.halted = haltBool


# ===== Parameter =====

class Parameter:
  def __init__(self, address, value):
    self.address = address
    self.value = value


# ===== Instructions =====

class Instruction:
  opcode, numParameters = 0, 0

  def _nextInstr(self, intcode):
    return intcode.instrPtr + self.numParameters + 1
  
  def execute(self, intcode, parameters, input):
    pass


class PlusInstruction(Instruction):
  opcode, numParameters = 1, 3

  def execute(self, intcode, parameters):
    intcode.setValue(parameters[2].address, (parameters[0].value + parameters[1].value))
    return self._nextInstr(intcode)


class MultiplyInstruction(Instruction):
  opcode, numParameters = 2, 3

  def execute(self, intcode, parameters):
    intcode.setValue(parameters[2].address, (parameters[0].value * parameters[1].value))
    return self._nextInstr(intcode)

  
class InputInstruction(Instruction):
  opcode, numParameters = 3, 1
  
  def execute(self, intcode, parameters):
    intcode.setValue(parameters[0].address, intcode.getInput())
    return self._nextInstr(intcode)
  
  
class OutputInstruction(Instruction):
  opcode, numParameters = 4, 1
  
  def execute(self, intcode, parameters):
    intcode.setOutput(parameters[0].value)
    return self._nextInstr(intcode)
  

class JumpIfTrueInstruction(Instruction):
  opcode, numParameters = 5, 2
  
  def execute(self, intcode, parameters):
    return parameters[1].value if parameters[0].value != 0 else self._nextInstr(intcode)
  
  
class JumpIfFalseInstruction(Instruction):
  opcode, numParameters = 6, 2
  
  def execute(self, intcode, parameters):
    return parameters[1].value if parameters[0].value == 0 else self._nextInstr(intcode)


class LessThanInstruction(Instruction):
  opcode, numParameters = 7, 3
  
  def execute(self, intcode, parameters):
    intcode.setValue(parameters[2].address, int(parameters[0].value < parameters[1].value))
    return self._nextInstr(intcode)
  
  
class EqualsInstruction(Instruction):
  opcode, numParameters = 8, 3
  
  def execute(self, intcode, parameters):
    intcode.setValue(parameters[2].address, int(parameters[0].value == parameters[1].value))
    return self._nextInstr(intcode)


class HaltInstruction(Instruction):
  opcode, numParameters = 99, 0

  def execute(self, intcode, parameters):
    intcode.setHalted(True)
    return None

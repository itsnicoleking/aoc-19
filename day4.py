# Part 1
def hasDoubleDigits(strArr):
  for i in range(len(strArr)-1):
    if strArr[i] == strArr[i+1]:
      return True
      break
  return False

def numsNeverDecrease(strArr):
  for i in range(len(strArr)-1):
    if int(strArr[i]) > int(strArr[i+1]):
      return False
      break
  return True
 
passCount = 0   
for i in range(125730, 579381):
  strArr = list(str(i))
  if hasDoubleDigits(strArr) and numsNeverDecrease(strArr):
    passCount += 1
    
print('Part 1:', passCount)
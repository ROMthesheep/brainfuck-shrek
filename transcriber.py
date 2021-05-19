from os import read

def writeBrainFuckInFile(n,d,file):
  print(n)
  file.write(">>")
  for counter in range(n//d):
    file.write("+")
  file.write("[<")
  for counter in range(d):
    file.write("+")
  file.write(">-]<.")

def makeCharacterLoop(number, file):
  if number > 255:
    return

    # Aqui es cuando me pregunto xq cojones python no tiene estructuras switch

  if (number%61==0  and number!= 61):
    writeBrainFuckInFile(number,61,file)
    return

  if (number%59==0  and number!= 59):
    writeBrainFuckInFile(number,59,file)
    return

  if (number%53==0  and number!= 53):
    writeBrainFuckInFile(number,53,file)
    return

  if (number%47==0  and number!= 47):
    writeBrainFuckInFile(number,47,file)
    return

  if (number%43==0  and number!= 43):
    writeBrainFuckInFile(number,43,file)
    return

  if (number%41==0  and number!= 41):
    writeBrainFuckInFile(number,41,file)
    return

  if (number%37==0  and number!= 37):
    writeBrainFuckInFile(number,37,file)
    return

  if (number%31==0  and number!= 31):
    writeBrainFuckInFile(number,31,file)
    return

  if (number%29==0  and number!= 29):
    writeBrainFuckInFile(number,29,file)
    return

  if (number%23==0  and number!= 23):
    writeBrainFuckInFile(number,23,file)
    return

  if (number%19==0  and number!= 19):
    writeBrainFuckInFile(number,19,file)
    return

  if (number%17==0  and number!= 17):
    writeBrainFuckInFile(number,17,file)
    return

  if (number%13==0  and number!= 13):
    writeBrainFuckInFile(number,13,file)
    return

  if (number%11==0  and number!= 11):
    writeBrainFuckInFile(number,11,file)
    return

  if (number%7==0  and number!= 7):
    writeBrainFuckInFile(number,7,file)
    return

  if (number%8==0 and number!= 8):
    writeBrainFuckInFile(number,8,file)
    return

  if (number%5==0 and number!= 5):
    writeBrainFuckInFile(number,5,file)
    return

  if (number%4==0 and number!= 4):
    writeBrainFuckInFile(number,4,file)
    return

  if (number%3==0 and number!= 3):
    writeBrainFuckInFile(number,3,file)
    return

  if (number%2==0 and number!= 2):
    writeBrainFuckInFile(number,2,file)
    return
  
  file.write(">>")
  for i in range(number//10):
    file.write("+")
  file.write("[<")
  for i in range(10):
    file.write("+")
  file.write(">-]<")
  for i in range(number - (number//10)*10):
    
    file.write("+")
  file.write(".")

  return
  

file = open("inputs/yourText.txt")
fileText = file.readlines()
outputFile = open("outputs/result.txt", "w")

for phrases in fileText:
  for c in phrases:
    makeCharacterLoop(ord(c),outputFile)

file.close()
outputFile.close()


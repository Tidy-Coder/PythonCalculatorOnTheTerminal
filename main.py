# A simple calculator on the terminal...
# I'm getting started to code...
# Thank you for download or utilisation in program or watch...
print("Thank you for download or utilisation in program or watch...")

print("Program made by TidyCodeur, if you want to know TidyCodeur's projects, search on github TidyCodeur...")

# Inform to program start
print("Program start...")

# Establish an array that contains the numbers from 0 to 9, in the form of a string.
stringNumberArray = []
for h in range(0, 10):
  stringNumberArray += str(h)

# Initialize an array that contains all valid characters/numbers/words.
allValid = stringNumberArray + [".", "*", "-", "+", "/", "modulo"]

# Print the valid characters/numbers/words.
print("The valid characters/numbers/words is " + ", ".join(["* (for multiplication)", "/ (for division)", "mudulo (no need to traduct you if you are learned python programming, i thing so, else if you don't know, modulo is the rest of a division)", "+", "-"] + stringNumberArray + [". (the comma)"]) + "...")

def checkOperationSyntax(theEntranceH):
  theEntranceD = theEntranceH.replace("modulo", "%")
  tidyArrayOperators = ["%", "*", "/", "+", "-"]
  if theEntranceD[0] in tidyArrayOperators:
    print("An operation don't start by operator...")
    return False
  elif theEntranceD[-1] in tidyArrayOperators:
    print("An operation don't finish by operator...")
    return False
  else:
    theFirstChar = "number"
  for m in theEntranceD:
    if theFirstChar == "operator" and m in tidyArrayOperators:
      print("An operation don't contains multiple operators in the same place...")
      return False
    elif m in tidyArrayOperators:
      theFirstChar = "operator"
    else:
      theFirstChar = "number"
  return True
def tidyOneIn(tidyArrayA, tidyArrayB):
  print("TidyOne")
  if tidyArrayA != [] or len(tidyArrayA) == 1:
    for e in tidyArrayA:
      for eb in tidyArrayB:
        if e == eb:
          return False
  elif len(tidyArrayA) == 1:
    for ed in tidyArrayB:
      if ed == tidyArrayA[0]:
        return False
    return True
  elif tidyArrayA == []:
    return True
def checkChars(theEntranceZ, validCharsZ, validWordsZ):
  tidyIsOkay = 0
  localisationLetter = 0
  reservedPlaces = []
  for i in theEntranceZ:
    localisationWord = 0
    for b in validWordsZ:
      if len(b) <= len(theEntranceZ[localisationLetter:]):
        if theEntranceZ[localisationLetter:localisationLetter+len(b)] == b and tidyOneIn(reservedPlaces, range(localisationLetter, localisationLetter+len(b))):
          reservedPlaces += [range(localisationLetter, localisationLetter+len(b))]
          tidyIsOkay += len(b)
          localisationLetter += len(b) - 1
      localisationWord += 1
    localisationLetter += 1
  localisationLetter = 0
  for ib in theEntranceZ:
    for z in validCharsZ:
      if z == ib and localisationLetter not in reservedPlaces:
        reservedPlaces += [localisationLetter]
        tidyIsOkay += 1
    localisationLetter += 1
  if tidyIsOkay == len(theEntranceZ):
    return True
  else:
    return False

# Initialize function checkChars for check if a string/array/tuple... contains only characters/words/numbers... of a Array/String/tuple...
def checkCharsAndSyntax(theEntrance, validChars, validWords):
  if checkChars(theEntrance, validChars, validWords):
    print("You are enter valids chars/words/numbers...")
    if checkOperationSyntax(theEntrance):
      print("The syntax of your operation is valid...")
      return True
    return False
  print("The syntax of the operation it's not valid, and the entrance contains other only valid chars...")
  return False
# Entrance for operation...
entrance = input()
# Check if the operation entrance is valid or not, if not valid, recommence to ask entrance...
while entrance.replace(" ", "") == "" or not checkCharsAndSyntax(entrance.replace(" ", ""), allValid[:-1], [allValid[-1]]):
  print("Please enter valid operation...")
  ancientEntrance = entrance
  print("if you want to add chars to ancientEntrance, enter \"Entrance\" in the terminal, and enter the chars you want to add in left or right or left and right \"Entrance\"...")
  entrance = input()
  if "Entrance" in entrance or "entrance" in entrance:
    entrance = entrance.replace("Entrance", ancientEntrance).replace("entrance", ancientEntrance)

# After Check, doing the operation with eval function...
print(entrance + " = " + str(eval(entrance.replace("modulo", "%").replace(" ", ""))))


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
print("The valid characters/numbers/words is " + ", ".join(["* (for multiplication)", "/ (for division)", "mudulo (no need to traduct you if you are learned python programming, i thing so, else if you d'ont know, modulo is the rest of a division)", "+", "-"] + stringNumberArray + [". (the comma)"]) + "...")

# Initialize function checkChars for check if a string/array/tuple... contains only characters/words/numbers... of a Array/String/tuple...
def checkCharsAndSyntax(contentToCheck, toCheckChars = None, toCheckWords = None):
  def StartBy(wordOrLetter, theContentToCheckZ):
    if len(wordOrLetter) == 1:
      if theContentToCheckZ[0] == wordOrLetter:
        return True
    else:
      if len(wordOrLetter) <= theContentToCheckZ:
        if theContentToCheckZ[0:len(wordOrLetter)+1] == wordOrLetter:
          return True
      else:
        return False
  def EachStartBy(theArrayZ, theContentToCheckZD):
    for ZD in theArrayZ:
      if StartBy(ZD, theContentToCheckZD):
        return True
    return False
  def CheckOperationSyntax(theContentToCheck):
    if EachStartBy(allValid[-7:], theContentToCheck):
      return False
    else:
      theLast = "number"
    for elementsZI in allValid[-7:]:
      if StartBy(elementsZI, theContentToCheck):
        theContentToCheckB = theContentToCheck[len(elementsZI)-1:]
        break
    localisationLetterZT = 0
    while localisationLetterZT < len(theContentToCheckB):
      if theLast == "operator" and EachStartBy(allValid[-7:], theContentToCheckB[localisationLetterZT:]):
        return False
      elif EachStartBy(allValid[-7:], theContentToCheckB[localisationLetterZT:]):
        for elementsTB in allValid[-7:]:
          if StartBy(elementsTB, theContentToCheckB[localisationLetterZT:]):
            localisationLetterZT += len(elementsTB)-1
            break
        theLast = "operator"
      elif theContentToCheckB[localisationLetterZT] in stringNumberArray:
        theLast = "number"
      localisationLetterZT += 1
    return True
  def CheckIfNoReservedPlaceHere(theReservedPlace, allReservedPlaces):
    print("all reserved places: ", allReservedPlaces)
    if allReservedPlaces == []:
      return True
    else:
      allReservedPlacesA = []
      allReservedPlacesB = []
      alternateNum = False
      for m in allReservedPlaces:
        if alternateNum == False:
          allReservedPlacesA += [m]
          alternateNum == True
        else:
          allReservedPlacesB += [m - 1]
          alternateNum = False
      print(allReservedPlacesA)
      print(allReservedPlacesB)
      allReservedPlacesD = []
      for v in range(0, len(allReservedPlacesA)):
        allReservedPlacesD += range(allReservedPlacesA[v], allReservedPlacesB[v]+1)
      for n in range(theReservedPlace[0], theReservedPlace[1]+1):
        if n in allReservedPlacesD:
          return False
      return True
  if toCheckChars == None and toCheckWords == None:
    return None
  else:
    isOkay = 0
  if toCheckChars != None:
    for p in contentToCheck:
      for d in toCheckChars:
        if p == d:
          isOkay += 1
          break
  if toCheckWords != None:
    toCheckWordsB = list(toCheckWords)
    for y in toCheckWordsB:
      repeat = 0
      for iy in toCheckWordsB:
        if iy == y:
          repeat += 1
          if repeat > 1:
            iy = []
    reservedplaces = []
    for z in toCheckWordsB:
      print("toCheckWordsB:", toCheckWordsB)
      localistaionContent = 0
      for i in contentToCheck:
        if z[0] == i and len(z) <= len(contentToCheck[localistaionContent:]):
          if contentToCheck[localistaionContent:localistaionContent+len(z)] == z and CheckIfNoReservedPlaceHere((localistaionContent, localistaionContent+len(z)+1), reservedplaces):
            reservedplaces += [(localistaionContent, localistaionContent+len(z)+1)]
            isOkay += len(z)
        localistaionContent += 1
  if isOkay == len(contentToCheck):
    print("haha1")
    if CheckOperationSyntax(contentToCheck):
      print("haha2")
      return True
    else:
      return False
  else:
    print("haha3")
    return False
# Entrance for operation...
entrance = input()
# Check if the operation entrance is valid or not, if not valid, recommence to ask entrance...
while entrance.replace(" ", "") == "" or not checkCharsAndSyntax(entrance.replace(" ", ""), allValid[:-1], [allValid[-1]]):
  print("Please enter valid operation...")
  entrance = input()

# After Check, doing the operation with eval function...
print(entrance + " = " + str(eval(entrance.replace("modulo", "%").replace(" ", ""))))


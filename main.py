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
  def CheckOperationSyntax(theContentToCheck):
    if theContentToCheck[0] in allValid[-7:]:
      return False
    else:
      theLast = "number"
    for bk in theContentToCheck[1:]:
      if theLast == "operator" and bk in allValid[-7:]:
        return False
      elif bk in allValid[-7:]:
        theLast = "operator"
      elif bk in stringNumberArray:
        theLast = "number"
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
        print("Ok1")
        if z[0] == i and len(z) <= len(contentToCheck[localistaionContent:]):
          print("Ok2")
          if contentToCheck[localistaionContent:localistaionContent+len(toCheckWords)] == z and CheckIfNoReservedPlaceHere((localistaionContent, len(toCheckWords)+1), reservedplaces):
            print("Ok3")
            reservedplaces += [(localistaionContent, len(toCheckWords)+1)]
            isOkay += len(toCheckWords)
        localistaionContent += 1
  if isOkay == len(contentToCheck):
    if CheckOperationSyntax(contentToCheck):
      return True
  else:
    return False
# Entrance for operation...
entrance = input()
# Check if the operation entrance is valid or not, if not valid, recommence to ask entrance...
while entrance.replace(" ", "") == "" or not checkCharsAndSyntax(entrance.replace(" ", ""), allValid[:-1], [allValid[-1]]):
  print("Please enter valid operation...")
  entrance = input()

# After Check, doing the operation with eval function...
print(entrance + " = " + str(eval(entrance.replace("modulo", "%").replace(" ", ""))))

# A simple calculator on the terminal...
# I'm getting started to code...
# Thank you for download or utilisation in program or watch...

# Inform to program start
print("Program start...")

# Establish an array that contains the numbers from 0 to 9, in the form of a string.
stringNumberArray = []
while h in range(0, 10):
  stringNumberArray += str(h)

# Initialize an array that contains all valid characters/numbers/words.
allValid = stringNumberArray + ["*", "-", "+", "/", "modulo"]

# Print the valid characters/numbers/words.
print("The valid characters/numbers/words is " + ", ".join(["* (for multiplication)", "/ (for division)", "mudulo (no need to traduct you if you are learned python programming, i thing so, else if you d'ont know, modulo is the rest of a division)", "+", "-"] + StringNumberArray) + "...")

# Initialize function checkPlease for check if a string/array/tuple... contains only characters/words/numbers... of a Array/String/tuple...
def checkPlease(contentToCheck, toCheckChars = None, toCheckWords = None):
  def CheckIfNoReservedPlaceHere(TheReservedPlace, allReservedPlaces):
    allReservedPlacesA = []
    allReservedPlacesB = []
    alternateNum = False
    while m in allReservedPlaces:
      if alternateNum == False:
        allReservedPlacesA += [m]
        alternateNum == True
      else:
        allReservedPlacesB += [m - 1]
        alternateNum = False
    allReservedPlacesD = []
    while v in range(0, len(allReservedPlacesA)+1):
      allReservedPlacesD += range(allReservedPlacesA[v], allReservedPlacesB[v]+1)
    while n in range(TheReservedPlace[0], TheReservedPlace[1]+1):
      if n in allReservedPlacesD:
        return False
    return True
  if toCheckChars == None and toCheckWords == None:
    return None
  else:
    isOkay = 0
  if toCheckChars != None:
    while p in contentToCheck:
      while d in toCheckChars:
        if p == d:
          isOkay += 1
          break
  if toCheckWords != None:
    if type(toCheckWords) == tuple:
      toCheckWordsB = list(toCheckWords)
    else:
      toCheckWordsB = toCheckWords
    while y in toCheckWordsB:
      repeat = 0
      while iy in toCheckWordsB:
        if iy == y:
          repeat += 1
          if repeat > 1:
            iy = []
    while z in toCheckWords:
      localistaionContent = 0
      reservedplaces = ()
      while i in contentToCheck:
        if z[0] == i:
          if i[localistaionContent:len(toCheckWords)+1] == toCheckWords and CheckIfNoReservedPlaceHere((localistaionContent, len(toCheckWords)+1), reservedplaces):
            reservedplaces += (localistaionContent, len(toCheckWords)+1)
        localistaionContent += 1
  if isOkay == len(contentToCheck):
    return True
  else:
    return False

# Entrance for operation...
entrance = input()
# Check if the operation entrance is valid or not, if not valid, recommence to ask entrance...
while entrance == "" or checkPlease(entrance, ):
  print("Please enter valid operation...")
  entrance = input()

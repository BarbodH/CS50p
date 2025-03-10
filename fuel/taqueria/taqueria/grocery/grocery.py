firstList = []
secondList = []

while True:
    try:
        grocery = input()
        firstList.append(grocery)

        for item in firstList:
            if item not in secondList:
                secondList.append(item)

        # Convert items in secondList to uppercase
        for i in range(len(secondList)):
            secondList[i] = secondList[i].upper()

    except EOFError:
        for item in secondList:
            print(item)
        break

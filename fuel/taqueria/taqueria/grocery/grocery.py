firstList = []
secondList = []

while True:
    try:
        grocery = input()
        firstList.append(grocery)
        for item in firstList:
            if item not in secondList:
                secondList.append(item)

        for i in secondList:
            i.upper()

    except EOFError:
        print(i)
        break


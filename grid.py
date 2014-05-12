def grid():
    numCol = int(input("How many columns would you like?"))
    numRow = int(input("How many rows would you like?"))
    col = "| " * (numCol + 1)
    dashes = "-" * ((numCol * 2) + 1)
    print(dashes)
    for x in range(numRow):
        print(col)
        print(dashes)
grid()

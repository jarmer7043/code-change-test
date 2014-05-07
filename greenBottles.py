import time
bottles = 10
for x in range(0,bottles):
    print("{0} green bottles, hanging on the wall".format(bottles))
    time.sleep(1.5)
    print("{0} green bottles, hanging on the wall".format(bottles))
    time.sleep(1.5)
    print("And if 1 green bottle should acidentally fall,")
    time.sleep(1.5)
    print("There'll be {0} green bottles hanging on the wall.".format(bottles-1))
    time.sleep(1.5)
    bottles = bottles-1

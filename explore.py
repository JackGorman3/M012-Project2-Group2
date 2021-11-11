import random


def exploreOnly():
    C1 = []
    for i in range(100):
        a = random.normalvariate(9, 3)
        C1.append(a)
    # creates a list with all happiness values of C1 visit
    C1sum = 0
    for num in C1:
        C1sum = C1sum + num
    C1happy = C1sum
    # adds them all together and defines it as C1happy
    C2 = []
    for i in range(100):
        b = random.normalvariate(7, 5)
        C2.append(b)
    C2sum = 0
    for num in C2:
        C2sum = C2sum + num
    C2happy = C2sum
    C3 = []
    for i in range(100):
        c = random.normalvariate(11, 7)
        C3.append(c)
    C3sum = 0
    for num in C3:
        C3sum = C3sum + num
    C3happy = C3sum
    # 100 days on each cafeteria
    totalHappy = C1happy + C2happy + C3happy
    return totalHappy

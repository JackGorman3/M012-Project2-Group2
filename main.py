import random

def exploitOnly():
    #day1 -> c1,  day2 -> c2, day3 -> c3
    #297days towards the best cafeteria
    pass

def exploreOnly():
    C1 = []
    for i in range(100):
        a = random.normalvariate(9,3)
        C1.append(a)
    C1sum = 0
    for num in C1:
        C1sum = C1sum + num
    C1happy = C1sum / 100

    C2 = []
    for i in range(100):
        b = random.normalvariate(7,5)
        C2.append(b)
    C2sum = 0
    for num in C2:
        C2sum = C2sum + num
    C2happy = C2sum / 100

    C3 = []
    for i in range(100):
        c = random.normalvariate(11,7)
        C3.append(c)
    C3sum = 0
    for num in C3:
        C3sum = C3sum + num
    C3happy = C3sum / 100
    #100 days on each cafeteria

    print("FOR EXPLORE ONLY\nCafeteria 1 Happiness = " + str(C1happy) + "\nCafeteria 2 Happiness = " + str(C2happy) + "\nCafeteria 3 Happiness = " + str(C3happy))
    pass

def eGreedy(e):
    #day1 -> c1,  day2 -> c2, day3 -> c3
    #best cafeteria for most, e value split between the 3 cafeteria's
    pass

def simulation(t):
    pass

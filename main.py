import random


def exploitOnly():
    #day1 -> c1,  day2 -> c2, day3 -> c3
    #297days towards the best cafeteria
    tothap = 0                                  #tothap is the total happiness
    h1= 9                                       #lines 7-9 are the values for each average happines level
    h2= 7
    h3= 11
    s1= 3                                       #lines 10-12 are the values for each standard of deviation
    s2= 5
    s3= 7
    c1 = random.normalvariate(h1, s1)          #13-15 generates a random number between the mean and standard of deviatiom
    tothap = tothap + c1
    c2 = random.normalvariate(h2,s2)
    tothap = tothap + c2
    c3= random.normalvariate(h3, s3)
    tothap = tothap + c3
    max = 0
    if c1 > max:                                         #17-22 generating which has the highest happiness level.
        max = "c1"
    if c2>max:
        max = "c2"
    if c3>max:
        max = "c3"
    for i in range(297):                                         # loop will run for the next 297 days since we already wenrt to each cafitrea first three days
        if max == "c1":
            c1hap = random.normalvariate(h1, s1)                # c1happ is the happines for the first caffieteria
            tothap = tothap + c1hap
        elif max == "c2":
            c2hap = random.normalvariate(h2,s2)                          # c2happ is the happiness for c2
            tothap = tothap + c2hap
        elif max == "c3":
           c3hap =  random.normalvariate(h3, s3)                    #c3happ is the happiness for the 3rd caffiteria
           tothap = tothap + c3hap
    return tothap


def exploreOnly():
    C1 = []
    for i in range(100):
        a = random.normalvariate(9,3)
        C1.append(a)
     #creates a list with all happiness values of C1 visit
    C1sum = 0
    for num in C1:
        C1sum = C1sum + num
    C1happy = C1sum
    #adds them all together and defines it as C1happy

    C2 = []
    for i in range(100):
        b = random.normalvariate(7,5)
        C2.append(b)
    C2sum = 0
    for num in C2:
        C2sum = C2sum + num
    C2happy = C2sum

    C3 = []
    for i in range(100):
        c = random.normalvariate(11,7)
        C3.append(c)
    C3sum = 0
    for num in C3:
        C3sum = C3sum + num
    C3happy = C3sum
    #100 days on each cafeteria
    totalHappy = C1happy + C2happy + C3happy
    #totalHappy is the sum of all visits of each cafeteria

    print("FOR EXPLORE ONLY\nCafeteria 1 Happiness = " + str(C1happy) + "\nCafeteria 2 Happiness = " + str(C2happy) + "\nCafeteria 3 Happiness = " + str(C3happy))
    print("Total Happiness = " + str(totalHappy))
    #print statement for reference, shows values when you run the function
    pass

def eGreedy(e):
    #day1 -> c1,  day2 -> c2, day3 -> c3
    #best cafeteria for most, e value split between the 3 cafeteria's
    pass

def simulation(t):
    pass

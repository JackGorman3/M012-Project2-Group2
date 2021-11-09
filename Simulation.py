import random

def eGreedy(e: int) -> int:
    totHap = 0
    per = e // 100  # e as a percentage
    c1Hap = random.normalvariate(9, 3)  # first visit to caf 1
    hap1 = c1Hap  # hap(1-3) is the variable that tracks the total hap for respective caf
    c2Hap = random.normalvariate(7, 5)  # first visit to caf 2
    hap2 = c2Hap
    c3Hap = random.normalvariate(11, 7)  # first visit to caf 3
    hap3 = c3Hap
    if c1Hap > c2Hap and c1Hap > c3Hap:  # next three if/elif/else statments establish the best caf after first three days
        best = c1Hap
        bestCaf = "c1"
    elif c2Hap > c1Hap and c2Hap > c3Hap:
        best = c2Hap
        bestCaf = "c2"
    else:
        best = c3Hap
        bestCaf = "c3"
    totHap = totHap + best

    for i in range(297):
        r = random.random()  # generates the random number between 0-1
        if r < per:  # this if statement is for when you are picking a random caf
            caf = random.randint(1, 3)
            if caf == 1:
                c1Hap = random.normalvariate(9, 3)
                totHap = totHap + c1Hap
                hap1 = hap1 + c1Hap
            elif caf == 2:
                c2Hap = random.normalvariate(7, 5)
                totHap = totHap + c2Hap
                hap2 = hap2 + c2Hap
            elif caf == 3:
                c3Hap = random.normalvariate(11, 7)
                totHap = totHap + c3Hap
                hap3 = hap3 + c3Hap
        else:  # this else is running the best caf when r > per (e%)
            if bestCaf == "c1":
                c1Hap = random.normalvariate(9, 3)
                totHap = totHap + c1Hap
                hap1 += c1Hap
            elif bestCaf == "c2":
                c2Hap = random.normalvariate(7, 5)
                totHap = totHap + c2Hap
                hap2 += c2Hap
            elif bestCaf == "c3":
                c3Hap = random.normalvariate(11, 7)
                totHap = totHap + c3Hap
                hap3 += c3Hap
        if hap1 > hap2 and hap1 > hap3:  # next three if statements resets what the best caf is after each run of the for loop
            bestCaf = "c1"
        elif hap2 > hap1 and hap2 > hap3:
            bestCaf = "c2"
        elif hap3 > hap2 and hap3 > hap1:
            bestCaf = "c3"
    return totHap


def exploitOnly():
    # day1 -> c1,  day2 -> c2, day3 -> c3
    # 297days towards the best cafeteria
    tothap = 0  # tothap is the total happiness
    h1 = 9  # lines 7-9 are the values for each average happines level
    h2 = 7
    h3 = 11
    s1 = 3  # lines 10-12 are the values for each standard of deviation
    s2 = 5
    s3 = 7
    c1 = random.normalvariate(h1, s1)  # 13-15 generates a random number between the mean and standard of deviatiom
    tothap = tothap + c1
    c2 = random.normalvariate(h2, s2)
    tothap = tothap + c2
    c3 = random.normalvariate(h3, s3)
    tothap = tothap + c3
    maxH = 0
    if c1 > maxH:  # 17-22 generating which has the highest happiness level.
        max = "c1"
    elif c2 > maxH:
        max = "c2"
    elif c3 > maxH:
        max = "c3"
    for i in range(297):  # loop will run for the next 297 days since we already wenrt to each cafitrea first three days
        if max == "c1":
            c1hap = random.normalvariate(h1, s1)  # c1happ is the happines for the first caffieteria
            tothap = tothap + c1hap
        elif max == "c2":
            c2hap = random.normalvariate(h2, s2)  # c2happ is the happiness for c2
            tothap = tothap + c2hap
        elif max == "c3":
            c3hap = random.normalvariate(h3, s3)  # c3happ is the happiness for the 3rd caffiteria
            tothap = tothap + c3hap
    return tothap


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


def simulation(t, e):
    # Optimum Happiness

    optHap = 11 * 300  # C3 has best average happiness
    # Expected Happiness and Regret Value
    expectedExploreHap = 9 * 100 + 7 * 100 + 11 * 100
    expectedExploitHap = 9 + 7 + 11 + 11 * 297
    expectedEGreedyHap = 11 * 264 + 7 * 12 + 9 * 12 + 12 * 11

    # c1 avg hap = 9
    # c2 avg hap = 7
    # c3 avg hap = 11

    # ExpectedRegret (Optimum Happiness - Total Happiness)
    expectedExploreRegret = optHap - expectedExploreHap
    expectedExploitRegret = optHap - expectedExploitHap
    expectedEGreedyRegret = optHap - expectedEGreedyHap

    # Loop through t times and calculate the average happiness values
    # for each function.
    exploreH = 0
    exploitH = 0
    eGreedyH = 0
    for i in range(t):
        exploreH = exploreH + exploreOnly()
        exploitH = exploitH + exploitOnly()
        eGreedyH = eGreedyH + eGreedy(e)

    exploreH = exploreH / t
    exploitH = exploitH / t
    eGreedyH = eGreedyH / t

    exploreR = optHap - exploreH
    exploitR = optHap - exploitH
    eGreedyR = optHap - eGreedyH

    print("Optimum Happiness: ", optHap)

    print("Explore Only Values: ")
    print("Expected Happiness: ", expectedExploreHap, "Expected Regret: ", expectedExploreRegret)
    print("Average Happiness: ", exploreH, "Average Regret: ", exploreR)

    print("Exploit Only Values: ")
    print("Expected Happiness: ", expectedExploitHap, "Expected Regret: ", expectedExploitRegret)
    print("Average Happiness: ", exploitH, "Average Regret: ", exploitR)

    print("eGreedy Values: ")
    print("Expected Happiness: ", expectedEGreedyHap, "Expected Regret: ", expectedEGreedyRegret)
    print("Average Happiness: ", eGreedyH, "Average Regret: ", eGreedyR)

simulation(100, 12)

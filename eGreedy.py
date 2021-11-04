import random

def eGreedy(e: int) -> int:
    totHap = 0
    per = e // 100 # e as a percentage
    c1Hap = random.normalvariate(9, 3) # first visit to caf 1
    hap1 = c1Hap # hap(1-3) is the variable that tracks the total hap for respective caf
    c2Hap = random.normalvariate(7, 5) # first visit to caf 2
    hap2 = c2Hap
    c3Hap = random.normalvariate(11, 7) # first visit to caf 3
    hap3 = c3Hap
    if c1Hap > c2Hap and c1Hap > c3Hap: # next three if/elif/else statments establish the best caf after first three days
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
        if r < per:                     # this if statement is for when you are picking a random caf
            caf = random.randint(1, 3)
            if caf == 1:
                c1Hap = random.normalvariate(9,3)
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
        else:                               # this else is running the best caf when r > per (e%)
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
        if hap1 > hap2 and hap1 > hap3:        # next three if statements resets what the best caf is after each run of the for loop
            bestCaf = "c1"
        elif hap2 > hap1 and hap2 > hap3:
            bestCaf = "c2"
        elif hap3 > hap2 and hap3 > hap1:
            bestCaf = "c3"
    return totHap

print(eGreedy(12)) # runs eGreedy with 12 percent greedy

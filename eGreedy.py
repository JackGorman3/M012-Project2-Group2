import random

def eGreedy(e: int):
    opHap = 3000
    totHap = 0
    per = e // 100
    c1Hap = random.normalvariate(9, 3)
    hap1 = c1Hap
    c2Hap = random.normalvariate(7, 5)
    hap2 = c2Hap
    c3Hap = random.normalvariate(11, 7)
    hap3 = c3Hap
    if c1Hap > c2Hap and c1Hap > c3Hap:
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
        r = random.random()
        if r < per:
            caf = random.randint(1, 3)
            if caf == 1:
                c1Hap = random.normalvariate(9,3)
                totHap = totHap + c1Hap
                hap1 = hap1 + c1Hap
            if caf == 2:
                c2Hap = random.normalvariate(7, 5)
                totHap = totHap + c2Hap
                hap2 = hap2 + c2Hap
            if caf == 3:
                c3Hap = random.normalvariate(11, 7)
                totHap = totHap + c3Hap
                hap3 = hap3 + c3Hap
        else:
            if bestCaf == "c1":
                c1Hap = random.normalvariate(9, 3)
                totHap = totHap + c1Hap
            if bestCaf == "c2":
                c2Hap = random.normalvariate(7, 5)
                totHap = totHap + c2Hap
            if bestCaf == "c3":
                c3Hap = random.normalvariate(11, 7)
                totHap = totHap + c3Hap
        if hap1 > hap2 and hap1 > hap3:
            bestCaf = "c1"
        if hap2 > hap1 and hap2 > hap3:
            bestCaf = "c2"
        if hap3 > hap2 and hap3 > hap1:
            bestCaf = "c3"
    regret = opHap - totHap

def simulation(t, e):

    #Optimum Happiness

    optHap = 11*300 #C3 has best average happiness
    #Expected Happiness and Regret Value
    expectedExploreHap = 9*100 + 7*100 + 11*100
    expectedExploitHap = 9+7+11+11*297
    expectedEGreedyHap = 11*264+7*12+9*12+12*11


    #c1 avg hap = 9
    #c2 avg hap = 7
    #c3 avg hap = 11

    #ExpectedRegret (Optimum Happiness - Total Happiness)

    expectedExploreRegret = optHap - expectedExploreHap
    expectedExploitRegret = optHap - expectedExploitHap
    expectedEGreedyRegret = optHap - expectedEGreedyHap

    # Loop through t times and calculate the average happiness values
    #for each function.
    exploreH = 0
    exploitH = 0
    eGreedyH = 0
    for i in range(t):
        exploreH = exploreH + explore0nly()
        exploitH = exploitH + exploit0nly()
        eGreedyH = eGreedyH + eGreedy(e)

    exploreH = exploreH/t
    exploitH = exploitH/t
    eGreedyH = eGreedyH/t

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

    #eGreedy is the same thing because exploit, explore, and egreedy are trying to find happiness

simulation(10, 12)
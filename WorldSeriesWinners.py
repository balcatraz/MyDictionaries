def main():
    infile = open('WorldSeriesWinners.txt', 'r')

    year = 1903
    TeamsDict = dict()
    YearsDict = dict()

    for line in infile:
        if year == 1904 or year == 1994:
            YearsDict[year] = 'n/a'
            year += 1

        try:
            TeamsDict[line.rstrip('\n')] += 1
        except:
            TeamsDict[line.rstrip('\n')] = 1

        YearsDict[year] = line.rstrip('\n')

        year += 1

    userYear = input('Pick a year in between 1903 and 2009: \n')

    if YearsDict[int(userYear)] != 'n/a':
        print('Winning team in ' + str(userYear) + ': ' + str(YearsDict[int(userYear)]))
        print(YearsDict[int(userYear)] + ' has won the world series '
              + str(TeamsDict[YearsDict[int(userYear)]]) + ' times.')

    else:
        print('No World series occurred that year!')

main()
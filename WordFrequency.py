import csv


def main():
    infile = open('AI.txt', 'r')

    wordDict = dict()

    for seg in infile:
        for wordStr in seg.split():

            wordStr = wordStr.replace(',', '')
            wordStr = wordStr.replace('.', '')
            wordStr = wordStr.replace('\"', '')
            wordStr = wordStr.replace('(', '')
            wordStr = wordStr.replace(')', '')
            wordStr = wordStr.replace(':', '')
            wordStr = wordStr.replace(';', '')

            try:
                if wordDict[wordStr]:
                    wordDict[wordStr] += 1

            except:
                wordDict[wordStr] = 1

    for key in wordDict:
        print(key, end=': ')
        print(wordDict[key])


main()
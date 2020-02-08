import sys

def DigitHangman() :
    problemNum = getProblem()
    ranNum = []
    score = 0
    printPattern(problemNum, ranNum)
    for i in range(5) :
        inputNumber = sys.stdin.readline()
        ranNum.append(inputNumber.split().pop())
        score = printPattern(problemNum, ranNum)
    print(score)
        

def getProblem() :
    inputStr = sys.stdin.readline()
    inputList = inputStr.split()
    return inputList

def printPattern(problemNum, ranNum) :
    score = 0
    for num in problemNum :
        if num in ranNum :
            print(num, end = ' ')
            score += 1
        else :
            print('_', end = ' ')
    for eachRanNum in ranNum :
        if eachRanNum not in problemNum :
            print(eachRanNum, end = ' ')
    print()
    return score

DigitHangman()
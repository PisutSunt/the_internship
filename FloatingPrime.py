import sys

def FloatingPrime() :
    while True :
        while True :
            sys.stdin.flush()
            inputStr = sys.stdin.readline()
            strLength = len(inputStr) - 1
            indexPoint = inputStr.index('.') + 1
            if strLength - indexPoint <= 12 :
                break
        inputNum = (float)(inputStr)
        if inputNum == 0.0 :
            break
        result = False
        for i in range(1, 4) :
            resultTemp = isPrime((int)(inputNum * 10**i))
            if resultTemp :
                result = result | resultTemp
        print(result)
    
def isPrime(num) :
    if num == 1 :
        return False
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True

FloatingPrime()

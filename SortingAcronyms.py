import sys

def sortAcronyms() :
    suffer = []
    suffer = getSuffer(suffer)
    detectedStr = detectUpper(suffer)
    detectedStr.sort()
    detectedStr.sort(key=sortStr, reverse=True)
    for str in detectedStr :
        print(str)

def getSuffer(suffer) :
    sys.stdin.flush()
    n = sys.stdin.readline()
    n = (int)(n)
    for i in range(0, n) :
        strInput = sys.stdin.readline().strip('\n')
        suffer.append(strInput)
    return suffer

def detectUpper(suffer) :
    detectedStr = []
    for str in suffer :
        detectedWord = ''
        splitedStr = str.split()
        for itr in splitedStr :
            if itr[0].isupper() :
                detectedWord = detectedWord + (itr[0])
        detectedStr.append(detectedWord)
    return detectedStr

def sortStr(e) :
    return len(e)

sortAcronyms()
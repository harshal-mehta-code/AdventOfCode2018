import collections
def findCheckSum(boxIds):
    numOfBoxWithTwoRepeatingLetters = 0
    numOfBoxWithThreeRepeatingLetters = 0
    for boxId in boxIds:
        c = collections.Counter(boxId)
        if(2 in c.values()):
            numOfBoxWithTwoRepeatingLetters+=1
        if(3 in c.values()):
            numOfBoxWithThreeRepeatingLetters+=1
    return numOfBoxWithThreeRepeatingLetters*numOfBoxWithTwoRepeatingLetters

def getCommonLetters(boxIds):
    commonLetters = ""
    for x,y in zip(boxIds[0],boxIds[1]):
        if x==y:
            commonLetters+=x
    return commonLetters

def dissimilarityScore(str1,str2):
    if(len(str1)!=len(str2)):
        return -1
    score = 0
    for x,y in zip(str1,str2):
        if x!=y:
            score+=1
    return score

def getBoxIdsWithOnlyOneDifferingLetter(boxIds):
    almostSameBoxIds = []
    for i in range(0,len(boxIds)-1):
        for j in range(i+1,len(boxIds)):
            id1, id2 = boxIds[i],boxIds[j]
            if(dissimilarityScore(id1,id2)==1):
                almostSameBoxIds.append(id1)
                almostSameBoxIds.append(id2)
    return almostSameBoxIds

if __name__ == "__main__":
    with open('input.txt') as f:
        boxIds = f.readlines()
        print(findCheckSum(boxIds))
        almostSimiarBoxIds = getBoxIdsWithOnlyOneDifferingLetter(boxIds)
        commonLetters = getCommonLetters(almostSimiarBoxIds)
        print(commonLetters)
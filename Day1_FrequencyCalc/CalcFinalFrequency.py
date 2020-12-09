import sys

def findFirstRepeatFrequency(freqChanges):
    startFreq = 0
    resultingFreqs = set([startFreq])
    repeatFreq = sys.maxsize
    while(repeatFreq not in resultingFreqs):
        for freq in freqChanges:
            nextFreq = startFreq + freq
            if(nextFreq in resultingFreqs):
                repeatFreq = nextFreq
                break
            resultingFreqs.add(nextFreq)
            startFreq = nextFreq
    return repeatFreq


if __name__ == "__main__":
    with open('input.txt') as f:
        freqChanges = [int(x) for x in f.readlines()]
        firstRepeatFrequency = findFirstRepeatFrequency(freqChanges)
        print(firstRepeatFrequency)
        
import itertools
import sys
#from itertools import combinations
import random

#def generate sample

if __name__ == '__main__':
    filename = sys.argv[1]
    supportNum = int(sys.argv[2])
    countIter = 1
    fraction = 0.4  # fraction of sample size
    sampleSupport = 0.9*fraction * supportNum
    check = True
    while check:
        sampleBasket = []
        frequentItemsets_candidates = []
        negative_border = set()
        # pass 1, count sample
        #print "testB"
        txt = open(filename)
        for line in txt:
            randomNum = random.random()
            if randomNum <= fraction:
                itemsEachBasket = line.strip().split(",")
                sampleBasket.append(itemsEachBasket)

        size = 1
        innerCheck = True
        frequentItemsets = []
        while innerCheck or size == 1:
            if size == 1:
                frequentSingleItem = []
                countSingleItem = {}
                for item in sampleBasket:
                    for i in item:
                        countSingleItem[i] = countSingleItem.setdefault(i, 0) + 1
                # generate frequent single
                for k, v in countSingleItem.iteritems():
                    if v >= sampleSupport:
                        frequentSingleItem.append(tuple(k))
                    else:
                        negative_border.add(k)

                frequentItemsets = sorted(frequentSingleItem)
                frequentItemsets_candidates.append(frequentItemsets)

            else:
                priorFrequentItemSets = frequentItemsets
                countFrequentItem = {}
                for item in sampleBasket:
                    sortedItem = sorted(item)
                    for subSet in itertools.combinations(sortedItem, size):
                        condition = True
                        for i in itertools.combinations(subSet, size-1):
                            if i not in priorFrequentItemSets:
                                condition = False
                                break
                        if condition:
                            countFrequentItem[subSet] = countFrequentItem.setdefault(subSet, 0) + 1
                temp = []
                tempPrint = []
                for k, v in countFrequentItem.iteritems():
                    if v >= sampleSupport:
                        temp.append(tuple(k))
                        tempPrint.append(list(k))
                    else:
                        condition2 = True
                        for subset in itertools.combinations(k, size - 1):
                            if subset not in priorFrequentItemSets:
                                condition2 = False
                        if condition2:
                            negative_border.add(k)

                frequentItemsets = sorted(temp)
                frequentItemsets_candidates.append(frequentItemsets)

            if len(frequentItemsets) == 0:
                innerCheck = False
                break
            else:
                size += 1

        #pass 2, whole file
        #check frequentItemsets_candidates
        countNegative = {}
        countAllSize = {}
        txt2 = open(filename)
        for line in txt2:
            eachLine = line.strip().split(",")
            for j in negative_border:
                if set(j) <= set(eachLine):
                    countNegative[j] = countNegative.setdefault(j, 0) + 1
            for item in frequentItemsets_candidates:
                for t in item:
                    if set(t) <= set(eachLine):
                        countAllSize[t] = countAllSize.setdefault(t, 0) + 1

        for k, v in countNegative.iteritems():
            if v >= supportNum:
                countIter += 1
                check = True
                break
        else:
            frequentAfterPassWholeFile = {}
            check = False
            print countIter
            print fraction
            for k, v in countAllSize.iteritems():
                if v >= supportNum:
                    frequentAfterPassWholeFile.setdefault(len(k), [])
                    frequentAfterPassWholeFile[len(k)].append(list(k))
            for k, v in frequentAfterPassWholeFile.iteritems():
                listTemp = sorted(v)
                print listTemp


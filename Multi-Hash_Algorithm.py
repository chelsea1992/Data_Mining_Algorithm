import sys
import itertools
from sys import argv
from itertools import combinations
from sets import Set


def firsthashfun(tuplex):
    total1 = 0
    for i in tuplex:
        for j in i:
            total1 += ord(j)
    return (firstInitialNum + total1) % bucketSize


def secondhashfun(tupley):
    total2 = 0
    for i in tupley:
        for j in i:
            total2 += ord(j)
    return (secondInitialNum + total2) % bucketSize


def generatebitmap(hashtablex):
    bitmap = 0
    for k in hashtablex:
        if hashtablex[k] >= supportNum:
            bitmap = bitmap | 1 << int(k)
    return bitmap


def bitmapSearch(bitmapx, tupleb, hashfunb):
    hashCodev = 1 << int(hashfunb(tupleb))
    if (hashCodev & bitmapx) != 0:
        return True
    else:
        return False


if __name__ == '__main__':

    filename = sys.argv[1]
    supportNum = int(sys.argv[2])
    bucketSize = int(sys.argv[3])

    baskets = []
    frequentSingleItem = []
    frequentItemsetsCandidates = {}
    countSingleDic = {}
    hashTable_1 = {}
    hashTable_2 = {}
    subItemSize = 1
    firstInitialNum = 100
    secondInitialNum = 180
    longestLine = 0
    size = 2
    priorFrequentItemSets = []
    frequentItemsets = []
    frequentSingleItemPrint = []
    # temp = []
    # tempPrint = []

    while len(frequentItemsets) > 0 or size == 2:
        txt = open(filename)
        # Pass 1
        if size == 2:
            for line in txt:
                itemsEachBasket = sorted(line.strip().split(","))
                for i in itemsEachBasket:
                    countSingleDic[i] = countSingleDic.setdefault(i, 0) + 1

                for subSet in itertools.combinations(itemsEachBasket, size):
                    hashCode1 = firsthashfun(subSet)
                    hashCode2 = secondhashfun(subSet)
                    hashTable_1[hashCode1] = hashTable_1.setdefault(hashCode1, 0) + 1
                    hashTable_2[hashCode2] = hashTable_2.setdefault(hashCode2, 0) + 1

            for k, v in countSingleDic.iteritems():
                if v >= supportNum:
                    frequentSingleItem.append(tuple(k))
                    frequentSingleItemPrint.append(k)

            frequentItemsets = sorted(frequentSingleItem)
            print(frequentSingleItemPrint)
        # Pass K
        else:
            print size - 2
            t_hashTable_1 = hashTable_1
            t_hashTable_2 = hashTable_2
            #print hashTable_1
            #print hashTable_2
            bitmap_1 = generatebitmap(hashTable_1)
            bitmap_2 = generatebitmap(hashTable_2)
            hashTable_1 = {}
            hashTable_2 = {}
            priorFrequentItemSets = frequentItemsets
            frequentItemsetsCandidates = {}
            #print priorFrequentItemSets
            for line in txt:
                itemsEachBasket = sorted(line.strip().split(","))
                for subSet in itertools.combinations(itemsEachBasket, size - 1):
                    sub_subSet = itertools.combinations(subSet, size - 2)
                    #print len(list(sub_subSet))
                    condition = True
                    for i in sub_subSet:
                        # print str(i)
                        # print str(priorFrequentItemSets)
                        if i not in priorFrequentItemSets:
                            condition = False
                            break

                    if bitmapSearch(bitmap_1, list(subSet), firsthashfun) and bitmapSearch(bitmap_2, list(subSet), secondhashfun) and condition:
                        frequentItemsetsCandidates[subSet] = frequentItemsetsCandidates.setdefault(subSet, 0) + 1

                for subSetToBeHashed in itertools.combinations(itemsEachBasket, size):
                    hashCode1 = firsthashfun(subSetToBeHashed)
                    hashCode2 = secondhashfun(subSetToBeHashed)
                    hashTable_1[hashCode1] = hashTable_1.setdefault(hashCode1, 0) + 1
                    hashTable_2[hashCode2] = hashTable_2.setdefault(hashCode2, 0) + 1

            # print str
            temp = []
            tempPrint = []
            for k, v in frequentItemsetsCandidates.iteritems():
                # print k, v
                if v >= supportNum:
                    temp.append(tuple(k))
                    tempPrint.append(list(k))
            frequentItemsets = sorted(temp)
            #print str(frequentItemsets)
            if len(tempPrint) != 0:
                print t_hashTable_1
                print t_hashTable_2
                print sorted(tempPrint)
                print
        # print size
        if len(frequentItemsets) == 0:
            txt.close()
            sys.exit()
        else:
            size += 1

import math


class LossyCounting:
    def __init__(self, minSupport, error):
        self.minSupport = minSupport
        self.error = error
        self.frequencies = {}
        self.maxPossibleError = {}
        self.bucketCounter = 1
        self.totalProcessElements = 0
        self.currentWindow = []

    def processNextElement(self, element):
        self.currentWindow.append(element)
        if len(self.currentWindow) >= (1 / self.error):
            self.processCurrentWindow()
            self.currentWindow = []

    def processCurrentWindow(self):
        for item in self.currentWindow:
            self.incrementItem(item)
            self.totalProcessElements += 1

        self.decrementAllFrequencies()
        self.deleteSmallFrequencies()
        self.bucketCounter += 1

    def incrementItem(self, item):
        if item in self.frequencies:
            self.frequencies[item] += 1
        else:
            self.frequencies[item] = 1
            self.maxPossibleError[item] = self.getCurrentBucketLabel() - 1

    def decrementAllFrequencies(self):
        for item in self.frequencies.keys():
            self.frequencies[item] -= 1

    def deleteSmallFrequencies(self):
        smallFrequenciesItems = list()

        currentBucketLabel = self.getCurrentBucketLabel()
        for (key, value) in self.frequencies.items():
            if value + self.maxPossibleError[key] <= currentBucketLabel:
                smallFrequenciesItems.append(key)

        for item in smallFrequenciesItems:
            del self.frequencies[item]
            del self.maxPossibleError[item]

    def getCurrentBucketLabel(self):
        return math.ceil(self.bucketCounter * self.error)

    def getFrequentItems(self):
        return {k: v for k, v in self.frequencies.items() if v >= (self.minSupport - self.error)*self.totalProcessElements }

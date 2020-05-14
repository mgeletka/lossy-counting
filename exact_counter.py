class ExactCounter:
    def __init__(self, minSupport):
        self.frequencies = {}
        self.minSupport = minSupport
        self.totalProcessElements = 0

    def processNextElement(self, item):
        if item in self.frequencies:
            self.frequencies[item] += 1
        else:
            self.frequencies[item] = 1

        self.totalProcessElements += 1

    def getFrequentItems(self):
        return {k: v for k, v in self.frequencies.items() if v >= self.minSupport * self.totalProcessElements}






from lossy_counting import LossyCounting
from exact_counter import ExactCounter

import re
import string
import numpy as np


class Demo:
    def __init__(self, minSupport, error):
        self.lossyCounter = LossyCounting(minSupport=minSupport, error=error)
        self.exactCounter = ExactCounter(minSupport=minSupport)

    def printOutput(self):
        sortedLossyCounter = {k: v for k, v in
                              sorted(self.lossyCounter.getFrequentItems().items(), key=lambda item: item[1],
                                     reverse=True)}
        sortedExactCounter = {k: v for k, v in
                              sorted(self.exactCounter.getFrequentItems().items(), key=lambda item: item[1],
                                     reverse=True)}

        print("Lossy count frequencies: " + str(sortedLossyCounter))
        print("Exact frequencies: " + str(sortedExactCounter))


class ExponentialDistributionDemo(Demo):
    def start(self):
        numberOfElements = 1000000
        for i in range(numberOfElements):
            randomElement = round(np.random.exponential(scale=0.5))
            self.lossyCounter.processNextElement(randomElement)
            self.exactCounter.processNextElement(randomElement)


class WareHouseDemo(Demo):
    def start(self):
        with open("retail.dat") as file:
            line = file.readline()
            while line:
                line = line.strip(' \n')
                data = line.split(" ")
                for item in data:
                    self.lossyCounter.processNextElement(item)
                    self.exactCounter.processNextElement(item)
                line = file.readline()


class RomeoAndJulietDemo(Demo):
    def start(self):
        with open("romeoAndJuliet.txt") as file:
            line = file.readline()
            while line:
                line = line.lower()
                line = re.sub(r'\d+', '', line)  # remove numbers
                line = line.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
                line = line.strip(' \n')
                if line == '':  # skip empty line
                    line = file.readline()
                    continue

                data = line.split(" ")
                for item in data:
                    self.lossyCounter.processNextElement(item)
                    self.exactCounter.processNextElement(item)
                line = file.readline()

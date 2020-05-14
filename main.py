from demo import WareHouseDemo, RomeoAndJulietDemo, ExponentialDistributionDemo

if __name__ == '__main__':
    print("Random exponential demo")
    randomExponentialDemo = ExponentialDistributionDemo(minSupport=0.01, error=0.001)
    randomExponentialDemo.start()
    randomExponentialDemo.printOutput()
    print("-----------------------------------------\n")

    print("Warehouse demo")
    wareHouseDemo = WareHouseDemo(minSupport=0.01, error=0.001)
    wareHouseDemo.start()
    wareHouseDemo.printOutput()
    print("-----------------------------------------\n")

    print("Romeo and Juliet demo")
    romeoAndJulietDemo = RomeoAndJulietDemo(minSupport=0.01, error=0.001)
    romeoAndJulietDemo.start()
    romeoAndJulietDemo.printOutput()
    print("-----------------------------------------\n")


class Laptop:

    ramOptions = {
        4: 0,
        8: 50,
        16: 100,
        32: 200
    }

    ssdOptions = {
        256: 0,
        512: 30,
        1024: 100
    }

    def __init__(self, brand, basePrice):
        self.brand = brand
        self.basePrice = basePrice
        self.ram = 4
        self.ssd = 256

    def getBrand(self):
        return self.brand
    
    def setBrand(self, brand):
        self.brand = brand

    def getRam(self):
        return self.ram

    def getPrice(self):
        ramPrice = self.ramOptions[self.ram]
        ssdPrice = self.ssdOptions[self.ssd]
        return self.basePrice + ramPrice + ssdPrice

    def setRam(self, ram):
        if ram in self.ramOptions:
            self.ram = ram
    
    def getSsd(self):
        return self.ssd 
    
    def setSsd(self, ssd):
        if ssd in self.ssdOptions:
            self.ssd = ssd

    def getDetails(self):
        return [self.brand, self.ram, self.ssd, self.getPrice()]
    
    def getSsdOptions(self):
        return list(self.ssdOptions.keys())

    def getRamOptions(self):
        return list(self.ramOptions.keys())

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM and {self.ssd} GB SSD"
        output += f"priced at £{self.getPrice()}"
        return output
    
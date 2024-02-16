from backend.laptop import Laptop

class GamingLaptop(Laptop):

    gpuOptions = {
        "NVIDIA GTX 1650": 0,
        "NVIDIA RTX 3070": 250,
        "NVIDIA RTX 4080": 350,
        "AMD RX 6800M": 280
    }

    def __init__(self, brand, basePrice):
        super().__init__(brand, basePrice)
        self.gpu = "NVIDIA GTX 1650"

    def getGpu(self):
        return self.gpu

    def setGpu(self, gpu):
        if gpu in self.gpuOptions:
            self.gpu = gpu

    def getPrice(self):
        gpuPrice = self.gpuOptions[self.gpu]
        return super().getPrice() + gpuPrice
    
    def getDetails(self):
        return super().getDetails()[:-1] + [self.getPrice(), self.gpu]
    
    def getGpuOptions(self):
        return list(self.gpuOptions.keys())

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM "
        output += f"and {self.gpu} priced at £{self.getPrice()}"
        return output
    

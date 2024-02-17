
class ShoppingCart:

    def __init__(self):
        self.laptops = []
        self.total = 0

    def addLaptop(self, laptop):
        self.laptops.append(laptop)
        self.total += laptop.getPrice()

    def getLaptops(self):
        return self.laptops
    
    def getLaptopAtIndex(self, index: int):
        return self.laptops[index]

    def getTotal(self):
        return self.total
    
    def setTotal(self, total):
        self.total = total

    def __str__(self):
        output = "Shopping cart contains:\n"
        for laptop in self.laptops:
            output += f"{laptop}\n"
        output += f"Total price is £{self.total}"
        return output
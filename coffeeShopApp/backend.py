class CoffeeShop:
    
    def __init__(self):
        self.customers = []
        # Q1
        self.limit = 5

    def addCustomer(self, name):
        # Q1
        if len(self.customers) < self.limit:
            self.customers.append(name)

    def removeCustomerAt(self, index):
        del self.customers[index]

    def getCustomerAt(self, index):
        return self.customers[index]

    def getNumCustomers(self):
        return len(self.customers)
    
    # Q1
    def getLimit(self):
        return self.limit
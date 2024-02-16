from tkinter import *
from backend import CoffeeShop


class CoffeeShopApp:
    
    def __init__(self, coffeeShop):
        self.coffeeShop = coffeeShop

        self.win = Tk()
        self.win.title("Coffee Shop")

        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(
            row=0,
            column=0,
            padx=10,  # Optional padding to make the GUI look nicer
            pady=10,
        )

        self.newCustomerName = StringVar()

        self.customerWidgets = []

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self, disableAddButton=False):
        self.deleteAllCustomerWidgets()

        customerEntry = Entry(
            self.mainFrame,
            textvariable=self.newCustomerName
        )
        customerEntry.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )

        addCustomerButton = Button(
            self.mainFrame,
            text="Add",
            command=self.addCustomer,
            # Q1
            state='disabled' if disableAddButton else 'normal'
        )
        addCustomerButton.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        numCustomers = self.coffeeShop.getNumCustomers()
        for i in range(numCustomers):
            customer = self.coffeeShop.getCustomerAt(i)
            customerLabel = Label(
                self.mainFrame,
                text=customer
            )
            customerLabel.grid(
                row=i+1,
                column=0,
                padx=5,
                pady=5,
            )
            self.customerWidgets.append(customerLabel)

            removeCustomerButton = Button(
                self.mainFrame,
                text="Remove",
                command=lambda index=i: self.removeCustomer(index)
            )
            removeCustomerButton.grid(
                row=i+1,
                column=1,
                padx=5,
                pady=5,
            )
            self.customerWidgets.append(removeCustomerButton)

    def addCustomer(self):
        name = self.newCustomerName.get()
        self.coffeeShop.addCustomer(name)
        self.createWidgets(
            # Q1
            disableAddButton=self.coffeeShop.getNumCustomers() == self.coffeeShop.getLimit()
        )
        self.newCustomerName.set("")  # Clear the entry box

    def removeCustomer(self, index):
        self.coffeeShop.removeCustomerAt(index)
        self.createWidgets()

    def deleteAllCustomerWidgets(self):
        for widget in self.customerWidgets:
            widget.destroy()
        self.customerWidgets = []


def main():
    coffeeShop = CoffeeShop()

    coffeeShop.addCustomer("Alice")
    coffeeShop.addCustomer("Bob")
    coffeeShop.addCustomer("Charlie")

    app = CoffeeShopApp(coffeeShop)
    app.run()

main()

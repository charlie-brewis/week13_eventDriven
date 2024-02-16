from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, StringVar
from backend.shoppingCart import ShoppingCart
from backend.laptop import Laptop
from backend.gamingLaptop import GamingLaptop

class LaptopShopApp:

    def __init__(self, shoppingCart: ShoppingCart = ShoppingCart()):
        self.shoppingCart = shoppingCart

        self.root = Tk()
        self.root.title("Laptop Shop")
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()
        
    def run(self) -> None:
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self) -> None:
        numLaptops = len(self.shoppingCart.getLaptops())
        for i in range(numLaptops):
            self.addLaptopToFrame(i)
        addLaptopButton = Button(self.mainFrame, text="Add Laptop", command=self.addLaptop)
        addLaptopButton.grid(row=numLaptops, column=0, padx=5, pady=5, columnspan=7)

    def addLaptopToFrame(self, index: int) -> None:
        laptop = self.shoppingCart.getLaptopAtIndex(index)
        brand, ram, ssd, price, gpu = self.getLaptopDetails(laptop)
        brandLabel = Label(self.mainFrame, text=f"Brand: {brand}")
        brandLabel.grid(row=index, column=0, padx=5, pady=5)
        ramLabel = Label(self.mainFrame, text=f"RAM: {ram} GB")
        ramLabel.grid(row=index, column=1, padx=5, pady=5)
        ssdLabel = Label(self.mainFrame, text=f"SSD: {ssd} GB")
        ssdLabel.grid(row=index, column=2, padx=5, pady=5)
        priceLabel = Label(self.mainFrame, text=f"Price: £{price}")
        priceLabel.grid(row=index, column=3, padx=5, pady=5)
        if gpu:
            gpuLabel = Label(self.mainFrame, text=f"GPU: {gpu}")
            gpuLabel.grid(row=index, column=4, padx=5, pady=5)
        updateButton = Button(self.mainFrame, text="Update", command=lambda: self.updateLaptop(index))
        updateButton.grid(row=index, column=5, padx=5, pady=5)
        removeButton = Button(self.mainFrame, text="Remove", command=lambda: self.removeLaptop(index))
        removeButton.grid(row=index, column=6, padx=5, pady=5)

    def getLaptopDetails(self, laptop: Laptop) -> list:
        details = laptop.getDetails()
        if not isinstance(laptop, GamingLaptop):
            details.append(None)
        return details
    
    def addLaptop(self) -> None:
        pass
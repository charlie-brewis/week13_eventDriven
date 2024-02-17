from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, StringVar, IntVar, DoubleVar, OptionMenu
from backend.shoppingCart import ShoppingCart
from backend.laptop import Laptop
from backend.gamingLaptop import GamingLaptop
from frontend.laptopUpdateWindow import LaptopUpdateWindow

class LaptopShopApp:

    def __init__(self, shoppingCart: ShoppingCart = ShoppingCart()):
        self.shoppingCart = shoppingCart

        self.root = Tk()
        self.root.title("Laptop Shop")
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()

        # self.total = DoubleVar()
        # self.total.set(self.shoppingCart.getTotal())
        self.totalMessage = StringVar()
        self.totalMessage.set(f"Total: £{self.shoppingCart.getTotal()}")
        
    def run(self) -> None:
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self) -> None:
        totalLabel = Label(self.mainFrame, textvariable=self.totalMessage)
        totalLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=7)
        numLaptops = len(self.shoppingCart.getLaptops())
        for i in range(numLaptops):
            self.addLaptopToFrame(i)
        addLaptopButton = Button(self.mainFrame, text="Add Laptop", command=self.addLaptop)
        addLaptopButton.grid(row=numLaptops + 1, column=0, padx=5, pady=5, columnspan=7)

    def addLaptopToFrame(self, index: int) -> None:
        rowIndex = index + 1
        laptop = self.shoppingCart.getLaptopAtIndex(index)
        brand, ram, ssd, price, gpu = self.sanitiseLaptopDetails(laptop)
        brandLabel = Label(self.mainFrame, text=f"Brand: {brand}")
        brandLabel.grid(row=rowIndex, column=0, padx=5, pady=5)
        ramLabel = Label(self.mainFrame, text=f"RAM: {ram} GB")
        ramLabel.grid(row=rowIndex, column=1, padx=5, pady=5)
        ssdLabel = Label(self.mainFrame, text=f"SSD: {ssd} GB")
        ssdLabel.grid(row=rowIndex, column=2, padx=5, pady=5)
        priceLabel = Label(self.mainFrame, text=f"Price: £{price}")
        priceLabel.grid(row=rowIndex, column=3, padx=5, pady=5)
        if gpu:
            gpuLabel = Label(self.mainFrame, text=f"GPU: {gpu}")
            gpuLabel.grid(row=rowIndex, column=4, padx=5, pady=5)
        updateButton = Button(self.mainFrame, text="Update", command=lambda: self.updateLaptop(index))
        updateButton.grid(row=rowIndex, column=5, padx=5, pady=5)
        removeButton = Button(self.mainFrame, text="Remove", command=lambda: self.removeLaptop(index))
        removeButton.grid(row=rowIndex, column=6, padx=5, pady=5)

    def sanitiseLaptopDetails(self, laptop: Laptop) -> list:
        details = laptop.getDetails()
        if not isinstance(laptop, GamingLaptop):
            details.append(None)
        return details
        
    def updateLaptop(self, index: int = None) -> None:
        LaptopUpdateWindow(index, self.root, self.shoppingCart, self.refreshApp)
        
    def refreshApp(self) -> None:
        self.destroyWidgets()
        self.totalMessage.set(f"Total: £{self.shoppingCart.getTotal()}")
        self.createWidgets()

    def destroyWidgets(self) -> None:
        for widget in self.mainFrame.winfo_children():
            widget.destroy()


        

        
    
    def addLaptop(self) -> None:
        pass
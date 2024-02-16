from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, StringVar, OptionMenu
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
        
    def updateLaptop(self, index: int = None) -> None:
        if not index:
            laptop = Laptop("Dell", 999.99)
            self.shoppingCart.addLaptop(laptop)
        else:
            laptop = self.shoppingCart.getLaptopAtIndex(index)
        brand, ram, ssd, price, gpu = self.getLaptopDetails(laptop)
        
        updateWindow = Toplevel(self.root)
        updateWindow.title("Update Laptop")
        updateFrame = Frame(updateWindow)
        updateFrame.pack()

        # Do brand as entry

        # ssdLabel = Label(updateFrame, text="SSD")
        # ssdLabel.grid(row=0, column=0, padx=0, pady=5)
        # selectedSsd = StringVar()
        # brandOptionMenu = OptionMenu(
        #     updateFrame,
        #     selectedSsd,
        #     *laptop.getSsdOptions(),
        #     command= lambda _: laptop.setSsd(int(selectedSsd.get()))
        # )
        # brandOptionMenu.grid(row=1, column=0, padx=0, pady=5)
        self.addDropmenu(1, updateFrame, "RAM", "GB", laptop, lambda ram: laptop.setRam(ram))

    def addDropmenu(self, column: int, frame: Frame, label: str, units: str, laptop: Laptop, command: callable) -> None:
        label = Label(frame, text=f"{label} ({units})")
        label.grid(row=0, column=column, padx=0, pady=5)
        selected = StringVar()
        selected.set(laptop.getRam())
        optionMenu = OptionMenu(
            frame,
            selected,
            *laptop.getRamOptions(),
            command=command
        )
        optionMenu.grid(row=1, column=column, padx=0, pady=5)

        
    
    def addLaptop(self) -> None:
        pass
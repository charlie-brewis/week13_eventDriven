from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, StringVar, IntVar, DoubleVar, OptionMenu
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
        brandVar = StringVar()
        brandVar.set(brand)
        ramVar = IntVar()
        ramVar.set(ram)
        ssdVar = IntVar()
        ssdVar.set(ssd)
        priceVar = DoubleVar()
        priceVar.set(price)
        gpuVar = StringVar()
        gpuVar.set(gpu)
        
        
        updateWindow = Toplevel(self.root)
        updateWindow.title("Update Laptop")
        updateFrame = Frame(updateWindow)
        updateFrame.pack()

        brandLabel = Label(updateFrame, text=f"Brand: {brand}")
        brandLabel.grid(row=0, column=0, padx=5, pady=5)
        brandEntry = Entry(updateFrame, textvariable=brandVar)
        brandEntry.grid(row=1, column=0, padx=5, pady=0)
        
        self.addDropmenu(1, updateFrame, "RAM", "GB", laptop, laptop.getRamOptions, lambda ram: laptop.setRam(ram), ramVar, priceVar)
        self.addDropmenu(2, updateFrame, "SSD", "GB", laptop, laptop.getSsdOptions, lambda ssd: laptop.setSsd(ssd), ssdVar, priceVar)
        self.addDropmenu(3, updateFrame, "GPU", "", laptop, laptop.getGpuOptions, lambda gpu: laptop.setGpu(gpu), gpuVar, priceVar) if isinstance(laptop, GamingLaptop) else None

        self.refreshPrice(updateFrame, priceVar)

        submitButton = Button(updateFrame, text="Submit", command=lambda: self.submitUpdate(index, laptop, brandVar, ramVar, ssdVar, priceVar, gpuVar))
        submitButton.grid(row=5, column=0, padx=5, pady=5)
        
    def addDropmenu(self, column: int, frame: Frame, label: str, units: str, laptop: Laptop, optionsCommand: callable, command: callable, detailVar, priceVar: DoubleVar) -> None:
        label = Label(frame, text=f"{label} ({units})")
        label.grid(row=0, column=column, padx=5, pady=5)
        optionMenu = OptionMenu(
            frame,
            detailVar,
            *optionsCommand(),
            command=lambda _: self.updateDetail(detailVar, laptop, command, priceVar, frame)
        )
        optionMenu.grid(row=1, column=column, padx=5, pady=0)

    def refreshPrice(self, frame, priceVar) -> None:
        priceLabel = Label(frame, text=f"Price: £{priceVar.get()}")
        priceLabel.grid(row=4, column=0, padx=5, pady=5)
    
    def updateDetail(self, detailVar, laptop, command, priceVar, frame) -> None:
        detail = detailVar.get()
        command(detail)
        priceVar.set(laptop.getPrice())
        self.refreshPrice(frame, priceVar)

        

        
    
    def addLaptop(self) -> None:
        pass
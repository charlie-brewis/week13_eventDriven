from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, StringVar, IntVar, DoubleVar, OptionMenu
from backend.shoppingCart import ShoppingCart
from backend.laptop import Laptop
from backend.gamingLaptop import GamingLaptop

class LaptopUpdateWindow:
    def __init__(self, index: int, root: Tk, shoppingCart: ShoppingCart, refreshMainAppCommand: callable):
        self.root = root
        self.shoppingCart = shoppingCart
        self.refreshMainAppCommand = refreshMainAppCommand
        
        if not index:
            self.laptop = Laptop("Dell", 999.99)
            self.shoppingCart.addLaptop(self.laptop)
        else:
            self.laptop = self.shoppingCart.getLaptopAtIndex(index)
        self.brandVar, \
        self.ramVar, \
        self.ssdVar, \
        self.oldPrice, \
        self.gpuVar \
        = self.translateLaptopDetailsToVars(*self.sanitiseLaptopDetails())

        self.window = Toplevel(self.root)
        self.window.title("Update Laptop") 
        self.mainFrame = Frame(self.window)
        self.mainFrame.pack()
        self.createWidgets()

    def translateLaptopDetailsToVars(self, brand: str, ram: int, ssd: int, price: float, gpu: str) -> tuple:
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
        return brandVar, ramVar, ssdVar, priceVar, gpuVar

    def createWidgets(self) -> None:
        brandLabel = Label(self.mainFrame, textvariable=self.brandVar)
        brandLabel.grid(row=0, column=0, padx=5, pady=5)
        brandEntry = Entry(self.mainFrame, textvariable=self.brandVar)
        brandEntry.grid(row=1, column=0, padx=5, pady=0)
        
        self.addDropmenu(1, "RAM", "GB", self.laptop.getRamOptions, lambda ram: self.laptop.setRam(ram), self.ramVar)
        self.addDropmenu(2, "SSD", "GB", self.laptop.getSsdOptions, lambda ssd: self.laptop.setSsd(ssd), self.ssdVar)
        self.addDropmenu(3, "GPU", "model", self.laptop.getGpuOptions, lambda gpu: self.laptop.setGpu(gpu), self.gpuVar) if isinstance(self.laptop, GamingLaptop) else None

        self.refreshPriceLabel()

        submitButton = Button(self.mainFrame, text="Submit", command=self.submitUpdate)
        submitButton.grid(row=5, column=0, padx=5, pady=5) 

    def addDropmenu(self, column: int, label: str, units: str, optionsCommand: callable, command: callable, detailVar) -> None:
        label = Label(self.mainFrame, text=f"{label} ({units})")
        label.grid(row=0, column=column, padx=5, pady=5)
        optionMenu = OptionMenu(
            self.mainFrame,
            detailVar,
            *optionsCommand(),
            command=lambda _: self.updateDetail(detailVar, command)
        )
        optionMenu.grid(row=1, column=column, padx=5, pady=0)
    
    def updateDetail(self, detailVar, command) -> None:
        detail = detailVar.get()
        command(detail)
        # self.priceVar.set(self.laptop.getPrice())
        self.refreshPriceLabel()

    def refreshPriceLabel(self) -> None:
        priceLabel = Label(self.mainFrame, text=f"Price: £{self.laptop.getPrice()}")
        priceLabel.grid(row=4, column=0, padx=5, pady=5)
    
    def sanitiseLaptopDetails(self) -> list:
        details = self.laptop.getDetails()
        if not isinstance(self.laptop, GamingLaptop):
            details.append(None)
        return details
    
    def submitUpdate(self) -> None:
        self.laptop.setBrand(self.brandVar.get())
        self.laptop.setRam(self.ramVar.get())
        self.laptop.setSsd(self.ssdVar.get())
        if isinstance(self.laptop, GamingLaptop):
            self.laptop.setGpu(self.gpuVar.get())
        print(f"old price: {self.oldPrice.get()}")
        print(f"new price: {self.laptop.getPrice()}")
        print()
        print(self.shoppingCart.getTotal())
        self.shoppingCart.setTotal(self.shoppingCart.getTotal() - self.oldPrice.get() + self.laptop.getPrice())
        print(self.shoppingCart.getTotal())
        self.oldPrice.set(self.laptop.getPrice())
        self.refreshMainAppCommand()

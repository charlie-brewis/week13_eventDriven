from backend import RecipeBook
from tkinter import *

class RecipeBookApp:
    def __init__(self, recipeBook: RecipeBook = RecipeBook()) -> None:
        self.recipeBook = recipeBook

        self.root = Tk()
        self.root.title("Recipe Book")
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()
    
    def run(self) -> None:
        self.createWidgets()
        self.root.mainloop()
    
    def createWidgets(self) -> None:
        numRecipes = self.recipeBook.getNumOfRecipes()
        for i in range(numRecipes):
            self.addRecipeToFrame(i)

    def addRecipeToFrame(self, index: int) -> None:
        recipe = self.recipeBook.getRecipeByIndex(index)
        recipeTitleLabel = Label(self.mainFrame, text=recipe.getName())
        recipeTitleLabel.grid(row=index, column=0, padx=5, pady=5)
        recipeMinutesLabel = Label(self.mainFrame, text=f"{recipe.getminutesToCook()} mins")
        recipeMinutesLabel.grid(row=index, column=1, padx=5, pady=5)
        viewRecipeButton = Button(self.mainFrame, text="View Recipe", command=lambda: self.viewRecipe(index))
        viewRecipeButton.grid(row=index, column=2, padx=5, pady=5)
    

if __name__ == "__main__":
    recipeBook = RecipeBook()
    recipeBook.addRecipe("Spaghetti Bolognese", 30, "1. Boil water\n2. Add pasta\n3. Cook for 10 minutes\n4. Drain pasta\n5. Cook meat\n6. Add sauce\n7. Combine pasta and sauce")
    recipeBook.addRecipe("Chicken Curry", 45, "1. Cook chicken\n2. Add spices\n3. Add sauce\n4. Cook for 30 minutes\n5. Serve with rice")
    recipeBook.addRecipe("Vegetable Stir Fry", 20, "1. Cook vegetables\n2. Add sauce\n3. Cook for 10 minutes\n4. Serve with rice")

    app = RecipeBookApp(recipeBook)
    app.run()


class Recipe:
    def __init__(self, name: str, minutesToCook: int, instructions: str) -> None:
        self.name = name
        self.minutesToCook = minutesToCook
        self.instructions = instructions
    
    def getName(self) -> str:
        return self.name
    
    def getminutesToCook(self) -> list[str]:
        return self.minutesToCook
    
    def getInstructions(self) -> str:
        return self.instructions
    
    def getDetails(self) -> tuple[str, int, str]:
        return (self.name, self.minutesToCook, self.instructions)
    

class RecipeBook:
    def __init__(self) -> None:
        self.recipes = []

    def addRecipe(self, name: str, minutesToCook: int, instructions: str) -> None:
        newRecipe = Recipe(name, minutesToCook, instructions)
        self.recipes.append(newRecipe)

    def getNumOfRecipes(self) -> int:
        return len(self.recipes)
    
    def getRecipeByIndex(self, index: int) -> Recipe:
        return self.recipes[index]
    

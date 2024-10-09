
# text based story thing lol

# inventory system - several items? use an array so user can type in input
# health bar - 
# simple crafting system? - 
# need specific items to progress
# list all details in a room
# commands [take, drop, inventory, look, score, quit, north, south, east, west, yes, no, health]

# possible items:
# weapon, armour, health potion, materials for crafting, score bonus?


# room a - starter room [summary: ] [doors to: b, c, d] [items: weapon, material, armour] [enemies: none] 
# room b -  room [summary: ] [doors to: a] [items:] [enemies:]
# room c -  room [summary: ] [doors to: a, e] [items:] [enemies:] 
# room d -  room [summary: ] [doors to: a, e] [items:] [enemies:] 
# room e -  room [summary: ] [doors to: c, d] [items:] [enemies:] 
# room f -  room [summary: ] [doors to: c, g] [items:] [enemies:] 
# room g -  room [summary: ] [doors to: f] [items:] [enemies:]
# room h -  room [summary: ] [doors to: end, f] [items:] [enemies:] 

# room layout
# _ h _
# g f _
# _ c e
# b a d

# testing
class textAdventure:
    def __init__(self):
        self.inventory = []
        self.health = 100
        self.score = 0
        self.validInputs = ["take", "drop", "inventory", "look", "score", "quit", "north", "south", "east", "west", "yes", "no", "health"]

        self.roomA_items = ["stick", 5]
        self.roomA_enemies = [("slime", 3, 3)]
        
    def inputParser(self, userInput):
        if userInput in self.validInputs:
            return True
        else:
            return False


    def startGame(self):
        gameRunning = True
        room = "roomA"
        print("You are an adventurer who is on a quest to find..")
        while gameRunning == True:
            match room:
                case "roomA":
                    print("You begin your adventure in a")
                    userInput = str(input("Input: "))
                case "roomB":
                    pass
                case "roomC":
                    pass
                case "roomD":
                    pass
                case "roomE":
                    pass
                case "roomF":
                    pass
                case "roomG":
                    pass
                case "roomH":
                    pass





if __name__ == "__main__":
    w = textAdventure()
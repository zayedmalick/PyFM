# Concept
from rich.console import Console


# Game Class to Start the Game
class Game():
    def __init__(self):
        # Variables
        self.console = Console()

    # Function to Leave Line
    def leave(self, num=1):
        for i in range(num):
            print()

    # Input Feauture with Styling
    def prompt(self, text, style):
        self.console.print(text, style=style, end="")
        inp = input()
        return inp

    # Starting the Game
    def start(self):
        
        # Greetings
        self.leave(num=2)
        self.console.print(
            "Welcome to Football Manager!",
            style="bold magenta"
        )

        # Option Menu
        self.leave(num=1)
        self.console.print(
            "Options : \n1. Transfer Market \n2. Team \n3. Exit",
            style="bold blue"
        )

        # Prompt for Choice
        self.leave()
        self.choice = self.prompt(
            "Enter Choice (1, 2, 3) : ",
            style="bold black"
        )

        # Extra Space
        self.leave(num=2)

        # Initiating Choice
        if self.choice == "1":
            # Transfer Market
            self.console.print(
                "Welcome to ",
                style="bold blue",
                end=""    
            )
            self.console.print(
                "Transfer Market !",
                style="bold red"
            )
            self.leave(2)

        elif self.choice == "2":
            # Transfer Market
            self.console.print(
                "Your Team ",
                style="bold blue",
                end=""    
            )
            self.leave(2)

        elif self.choice == "3":
            self.console.print(
                "Thank You for Playing Football Manager!",
                style="bold red"
            )
            self.leave(2)
            exit()

# Running the Game
if __name__ == "__main__":
    game = Game()
    game.start()
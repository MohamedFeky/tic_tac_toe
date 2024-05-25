class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self):
        while True:
            name = input("inter your name (letters only!) : ")
            if name.isalpha():
                self.name = name
                break
            print("invalde name plss the name only letters")
    
    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose ur symbol (one char!) : ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("just one char")

class Menu:
    def display_main_menu(self): # start game or quit game 
        print("hello in the X O game")
        print("choose 1 to start the game")
        print("choose 2 to quit the game")
        while True:
            try:
                choice = input("enter ur choice : ")
                break
            except ValueError:
                print("invaled input. pls enter 1 or 2")
        print(f"u enter number : {choice}")


    def display_endgame_menu(): # restart game quit game
        menu_text = """
        game over!
        press 1 to restart the game.
        press 2 to quit the game.
        enter ur choice 1 or 2 : """
        while True:
            try:
                choice = input(menu_text)
                break
            except ValueError:
                print("invaled input. pls enter 1 or 2")

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("- "*3)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False    

    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit() 
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


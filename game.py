from board import Board
import random

class Game:
    def __init__(self, playerX, playerO): # Initialize the game with a board and players
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO
        self._current_player = playerX
        self._result = False


    def _switch_player(self): # Switch the current player after each move
        if self._current_player == self._playerX:
            self._current_player = self._playerO
        else:
            self._current_player = self._playerX


    def run(self): # Set values for players and run the game loop
        self._playerX.set_value('X')
        self._playerO.set_value('O')
        while not self._result:
            print(self._board)
            try:
                x, y = self._current_player.get_move()
                self._board.set(x, y, self._current_player.get_value())
                self._result = self._board.check_winner()
                self._switch_player()
            except ValueError:
                print("Invalid imput, try again")
                continue
        print(self._board)
        print("Game Draw") if self._result == "draw" else print(f"{self._result} won!")
        

class Player:
    def __init__(self): # Initialize player with a value (X or O)
        self._value = None
    
    def __str__(self): # Return a string representation of the player's input
        return self._value

    def set_value(self, value):  # Set the value (X or O) for the player
        self._value = value

    def get_value(self): # Get the value of the player (X or O)
        return self._value

class Human(Player):
    def get_move(self): # Get the move from the human player through user input
        prompt = f"player {self._value} > "
        move = input(prompt) #this is a string
        x, y = [int(x) for x in move.split(",")]
        return x, y

class Bot(Player):
    def get_move(self): # Get a random move from the bot player
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        return x, y

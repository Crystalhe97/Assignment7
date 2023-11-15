from game import Game, Human, Bot

prompt = "Single or Double? "
player_number = input(prompt)

if player_number == 'Single':
    game = Game(Human(), Bot())
elif player_number == 'Double':
    game = Game(Human(), Human())
else:
    raise ValueError("Only Accept input \"Single\" or \"Double\"!")
game.run()
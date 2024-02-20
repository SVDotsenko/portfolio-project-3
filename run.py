# todo валидация что пользователь уже вводил эти координаты

# todo after game over print message
# todo read requirements, what else can be added
# todo write in description that indexing from 1
# todo add description to each method
# todo check the code thorough validator pip8online.com
# todo write readme.md

from src.board import ComputerBoard, HumanBoard
from src.new_game import new_game
from src.prompt import start

start()
new_game(HumanBoard(), ComputerBoard())

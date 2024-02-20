# todo read requirements, what else can be added
# todo check the code thorough validator pip8online.com
# todo write readme.md

from src.board import ComputerBoard, HumanBoard
from src.new_game import new_game
from src.utilities import welcome

welcome()
new_game(HumanBoard(), ComputerBoard())

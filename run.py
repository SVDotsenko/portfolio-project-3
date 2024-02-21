# todo write readme.md
# todo how check in pycharm if the code is good (pip8online.com)

from assets.py.board import ComputerBoard, HumanBoard
from assets.py.new_game import new_game
from assets.py.utilities import welcome

welcome()
new_game(HumanBoard(), ComputerBoard())

# todo more about manual testing (steps used to test it) https://github.com/KittyDig/Portfolio3
# todo deployment write up - how to clone, how you used git and git hub and how to got it running on heroku https://github.com/KittyDig/Portfolio3

from assets.py.board import ComputerBoard, HumanBoard
from assets.py.new_game import new_game
from assets.py.utilities import welcome

welcome()
new_game(HumanBoard(), ComputerBoard())

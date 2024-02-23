# todo delete extra spaces after description. set up pycharm for automatic formatting
# todo https://pep8ci.herokuapp.com
# todo more about manual testing (steps used to test it)
# todo deployment write up - how to clone, how you used git and git hub and how to got it running on heroku

from assets.py.board import ComputerBoard, HumanBoard
from assets.py.new_game import new_game
from assets.py.utilities import welcome

welcome()
new_game(HumanBoard(), ComputerBoard())

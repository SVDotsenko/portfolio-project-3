from src.board import Board
from src.enums import Player
from src.new_game import new_game
from src.prompt import start

start()
new_game(Board(4, Player.HUMAN), Board(4, Player.COMPUTER))

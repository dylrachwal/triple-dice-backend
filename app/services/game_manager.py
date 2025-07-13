from uuid import uuid4
from typing import Dict, List
import random
import string

MAX_PLAYERS = 4 

class Game:
    def __init__(self,players: List[str]=None, started: bool=False):
        self.players = players if players else []
        self.started = started
        self.id = str(uuid4())
        self.state = "waiting"
        self.rounds = [] 


games: Dict[str, Game] = {}

def create_game(host_name: str) -> str:
    code = generate_game_code()
    while code in games:
        code = generate_game_code()

    games[code] = Game(
        players=[host_name],
        started=False
    )
    return code



def join_game(game_code: str, player_name: str) -> bool:
    game = games.get(game_code)
    if not game:
        return False
    if len(game.players) >= MAX_PLAYERS or game.started:
        return False
    if player_name in game.players:
        return False
    game.players.append(player_name)

    # Lock the game if full
    if len(game.players) == MAX_PLAYERS:
        game.started = True

    return True

def end_game(code: str):
    if code in games:
        del games[code]

def generate_game_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
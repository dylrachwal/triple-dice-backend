from fastapi import APIRouter, HTTPException
from app.services.game_manager import create_game, join_game

router = APIRouter()

@router.post("/games/create")
def create_new_game(host_name: str):
    code = create_game(host_name)
    return {"code": code, "message": "Partie créée"}

@router.post("/games/{code}/join")
def join_game_by_code(code: str, player_name: str):
    success = join_game(code, player_name)
    if not success:
        raise HTTPException(status_code=400, detail="Impossible de rejoindre la partie.")
    return {"message": f"{player_name} a rejoint la partie {code}"}
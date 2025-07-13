from fastapi import FastAPI
from app.api import games

app = FastAPI()

app.include_router(games.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans le jeu de société Triple Dice 🎲"}
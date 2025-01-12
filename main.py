from fastapi import FastAPI
from nba_api.stats.endpoints import playercareerstats
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the NBA Analysis API"}

@app.get("/player/{player_id}")
async def get_player_career_stats(player_id: str):
    # Fetch player career stats using nba_api
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    # Convert the data to a dictionary
    data = career_stats.get_dict()
    return data

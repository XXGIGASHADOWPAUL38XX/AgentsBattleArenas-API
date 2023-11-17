from flask import Flask, request, jsonify
from Engine.character import CharacterProxy
from Engine.engine import Engine
from Engine.arena import Arena
app = Flask(__name__)

engine = Engine()
arenas = []

# /CHARACTER
@app.post("/character")
def create_character():
    data = request.json
    cid = data.get('cid')
    teamId = data.get('teamId')
    life = data.get('life')
    strength = data.get('strength')
    armor = data.get('armor')
    speed = data.get('speed')
    character = CharacterProxy(cid, teamId, life, strength, armor, speed)
    engine.addPlayer(character)
    return character.toDict()

@app.put("/character")
def edit_character():
    data = request.json
    cid = data.get('cid')
    teamId = data.get('teamId')
    life = data.get('life')
    strength = data.get('strength')
    armor = data.get('armor')
    speed = data.get('speed')
    character_to_edit = engine.getPlayerByName(cid)
    print(character_to_edit)
    return character_to_edit.toDict()

# /ARENA

@app.post("/arena")
def create_arena():
    arena = Arena()
    arenas.append(arena)
    return arena.toDict()

@app.get("/arena/<arenaid>")
def get_arena_characters(arenaid):
    return arenas[arenaid].toDict()

@app.post("/arena/enter")
def enter_arena():
    data = request.json
    player_cid = data.get('player_cid')
    arena_id = data.get('arena_id')
    arena = arenas[arena_id]
    character = engine.getPlayerByName(player_cid)
    arena.addPlayer(character)
    return arena.toDict()

# /ACTION
@app.post("/action")
def action():
    return "<p>Hello, World!</p>"

# /RUN
@app.post("/run")
def create_engine():
    return

@app.get("/run")
def get_engine_status():
    return "<p>Hello, World!</p>"
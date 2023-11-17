from flask import Flask, request, jsonify
from Engine.character import CharacterProxy
from Engine.engine import Engine
app = Flask(__name__)

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
    print(cid)
    engine = Engine()
    character_to_edit = engine.getPlayerByName(cid)
    print(character_to_edit)
    character = CharacterProxy(cid, teamId, life, strength, armor, speed)
    return character.toDict()

# /ARENA
@app.get("/arena/<arenaid>/")
def get_arena_characters(arenaid):
    return 'Hello world!' + arenaid

@app.post("/arena/enter")
def hello_world4():
    return "<p>Hello, World!</p>"

# /ACTION
@app.post("/action")
def hello_world5():
    return "<p>Hello, World!</p>"

# /RUN
@app.post("/run")
def hello_world6():
    return "<p>Hello, World!</p>"

@app.get("/run")
def hello_world7():
    return "<p>Hello, World!</p>"
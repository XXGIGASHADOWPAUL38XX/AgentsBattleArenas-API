from flask import Flask, request, jsonify
from Engine.character import CharacterProxy
from Engine.engine import Engine
from Engine.arena import Arena
app = Flask(__name__)

engine = Engine()
engine._arena = Arena(engine._data)

@app.post("/character/join")
def join_character():
    data = request.json
    cid = data.get('cid')
    teamId = data.get('teamId')
    life = data.get('life')
    strength = data.get('strength')
    armor = data.get('armor')
    speed = data.get('speed')
    try:
        character = CharacterProxy(cid, teamId, life, strength, armor, speed)
    except ValueError as e:
        return str(e)
    engine.addPlayer(character)
    engine._arena.addPlayer(character)
    return character.toDict()

@app.post("/character/action")
def set_character_action():
    data = request.json
    cid = data.get('cid')
    action = data.get('action')
    target = data.get('target')
    character_to_set_action: CharacterProxy = engine._arena.getPlayerByName(cid)
    if (character_to_set_action is None):
        return "Character not found"
    character_to_set_action.setAction(action)
    character_to_set_action.setTarget(target)
    return character_to_set_action.toDict()

@app.get("/character/<cid>")
def get_character(cid):
    character = engine._arena.getPlayerByName(cid)
    if (character is None):
        return "Character not found"
    return character.toDict()

@app.get("/characters")
def get_all_characters():
    characters = engine._arena._playersList
    characters_dict = {}
    for character in characters:
        characters_dict[character.getId()] = character.toDict()
    return characters_dict

@app.get("/status/<lap>")
def get_status(lap):
    return engine.getState()

def check_stats(life: int, strength: int, armor: int, speed: int):
    if (life + strength + armor + speed) > 20:
        return False
    return True

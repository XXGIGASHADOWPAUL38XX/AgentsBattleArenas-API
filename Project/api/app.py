from flask import Flask, request, jsonify
from Engine.character import CharacterProxy
from Engine.engine import Engine
from Engine.arena import Arena
app = Flask(__name__)

engine = Engine()
engine._arena = Arena(engine._data)

# /CHARACTER
@app.post("/character/join")
def join_character():
    data = request.json
    cid = data.get('cid')
    teamId = data.get('teamId')
    life = data.get('life')
    strength = data.get('strength')
    armor = data.get('armor')
    speed = data.get('speed')
    character = CharacterProxy(cid, teamId, life, strength, armor, speed)
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
    print(character_to_set_action)
    character_to_set_action.setAction(action)
    character_to_set_action.setTarget(target)
    return character_to_set_action.toDict()

@app.get("/character/<cid>")
def get_character(cid):
    return engine._arena.getPlayerByName(cid).toDict()

@app.get("/characters")
def get_all_characters():
    characters = engine._arena._playersList
    characters_dict = {}
    for character in characters:
        characters_dict[character.getId()] = character.toDict()
    return characters_dict

@app.post("/status")
def action():
    return "<p>Hello, World!</p>"
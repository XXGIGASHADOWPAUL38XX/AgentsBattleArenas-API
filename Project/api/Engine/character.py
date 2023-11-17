from random import randint
from Engine.action import *

class CharacterProxy:
    def __init__(self, cid :str, teamid :str, life :int, strength :int, armor :int, speed :int):
        self._id = cid
        self._teamid = teamid
        self._life = life
        self._strength = strength
        self._armor = armor
        self._speed = speed
        if self._total_stats() > 20:
            raise ValueError("Total stats (strength + life + armor + speed) cannot exceed 20.")
        if self._life < 0 or self._strength < 0 or self._armor < 0 or self._speed < 0:
            raise ValueError("Stats cannot be negative.")
        self._action = None
        self._target = None
        self._dead = False

    def isDead(self):
        return self._dead

    def isId(self, cid):
        return self._id == cid

    def getId(self):
        return self._id

    def getLife(self):
        return self._life

    def getStrength(self):
        return self._strength

    def getArmor(self):
        return self._armor

    def getSpeed(self):
        return self._speed

    def _total_stats(self):
        return self._life + self._strength + self._armor + self._speed

    def getAction(self):
        if self._action == ACTION.HIT or self._action == ACTION.FLY:
            return self._action, self._target
        return self._action, None

    def setLife(self, value):
        self._life = value
        if self._life <= 0:
            self._dead = True

    def setStrength(self, value):
        self._strength = value

    def setArmor(self, value):
        self._armor = value

    def setSpeed(self, value):
        self._speed = value

    def setAction(self, value):
        self._action = value
    
    def setTarget(self, value):
        self._target = value

    def __str__(self):
        s = "------------\n"
        s += "cid : " + self._id + ",\n"
        s += "life : " + str(self._life) + "\n"
        s += "strength : " + str(self._strength) + "\n"
        s += "armor : " + str(self._armor) + "\n"
        s += "speed : " + str(self._speed) + "\n"
        s += "------------\n"
        return s

    def toDict(self):
        cDict = {}
        cDict["cid"] = self._id
        cDict["teamid"] = self._teamid
        cDict["life"] = self._life
        cDict["strength"] = self._strength
        cDict["armor"] = self._armor
        cDict["speed"] = self._speed
        cDict["action"] = actionToStr(self._action)
        cDict["target"] = str(self._target)
        cDict["dead"] = self._dead
        return cDict

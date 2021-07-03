from pydantic import BaseModel
from typing import List, Optional


class Trait(BaseModel):
    id: str
    name: str


class Character(BaseModel):
    id: str
    name: str
    description: str
    portrait: str
    starItems: List[dict]  # if needed create sub type
    status: str
    unlockStars: int
    traits: List[Trait]
    abilityKit:dict
    gearTiers: dict

    def get_gear(self,gear_level:str="1"):
        return self.gearTiers.get(str(gear_level),{}).get("slots",[])
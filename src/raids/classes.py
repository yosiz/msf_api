from pydantic import BaseModel
from typing import List,Optional
class Room(BaseModel):
    name:Optional[str]
    description:Optional[str]
    icon:Optional[str]
    roomNW:Optional[str]
    requirements:Optional[dict]

    def room_req(self):
        req = {"traits":[],"iso8":None}
        if "anyCharacterFilters" in self.requirements:
            req["traits"] = [x for x in self.requirements["anyCharacterFilters"].get("allTraits",[])]
            req["iso8"] = self.requirements["anyCharacterFilters"].get("iso8ClassLevel",None)

class Raid(BaseModel):
    groupId: str
    id: str
    name: str
    description: str
    details: str
    keyCost: int
    hours: int
    teams: int
    maxPlayersPerTeam: int
    combatNodesPerTeam: int
    rayCount:int
    rayDepth:int
    rays: List
    rooms:Optional[dict]

    def get_map(self):
        return self.rays

    def get_rooms(self):
        return [Room(**x) for x in self.rooms.values()]
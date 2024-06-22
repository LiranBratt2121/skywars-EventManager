from dataclasses import dataclass


@dataclass
class PlayerData:
    wins: int
    kills: int
    assists: int
    top_3: int
    

    
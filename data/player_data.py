from dataclasses import dataclass, field


@dataclass
class PlayerData:
    name: str
    wins: int = field(default=0)
    kills: int = field(default=0)
    assists: int = field(default=0)
    top_3: int = field(default=0)
    

    
from dataclasses import dataclass
import typing import Union
import json
from fastapi import FastAPI


with open("pokemon.json", "r") as f:
    pokemons_list = json.load(f)


list_pokemons = {k+1:v for k, v in enumerate(pokemons_list)}


@dataclass
class Pokemon():
    id: int
    name: str
    types: list[str]
    total: int
    hp: int
    attack: int
    defense: int
    attack_special: int
    defense_special: int
    speed: int
    evolution_id: Union[int, None] = None


app = FastAPI()



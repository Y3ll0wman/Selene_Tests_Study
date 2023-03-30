import json

from pydantic import BaseModel


class Config(BaseModel):
    url: str
    login: str
    password: str


with open('../config.json') as json_file:
    data = json.load(json_file)

config = Config(**data)
import uuid
class objects():
    def __init__(thing, name, use):
        thing.name = name
        thing.use = use

class weapons(objects):
    def __init__(thing, name, use, attack):
        super().__init__(name, use)
        thing.attack = attack
    def str(thing):
        return f"{thing.name}, {thing.use}, {thing.attack}"

thing = "hebro"
name = "herro"
use = "hiiii"
attack = "dori"
yo = weapons
print(yo)
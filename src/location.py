from enum import Enum


class LocationEnum(Enum):
    TOWN = 0
    DUNGEON = 1


class Location:
    
    def __init__(self, name):
        self.name = name

    def get_description(self) -> str:
        return ""

    def get_options(self) -> str:
        return ""

    def process_input(self, user_input, system):
        return


class Town(Location):

    def __init__(self):
        super().__init__("Town")

    def get_description(self) -> str:
        return "The medieval of Oakhaven."

    def get_options(self) -> str:
        return "1: Rest\n2: Go to Dungeon"

    def process_input(self, user_input, system):
        match user_input:
            case 1:
                days_rested = system.rest()
                system.print_response(f"Describe how the player rests for {days_rested} day{"s" if days_rested > 1 else ""} in only one sentence.")
                print(f"Current HP: {system.player.hp} / {system.player.max_hp}")
            case 2:
                system.set_location(LocationEnum.DUNGEON)
                system.print_response("Describe how the player travels to the dungeon in only one sentence.")
            case _:
                print("Invalid input.")

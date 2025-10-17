from location import *
from item import *


class Room:

    description = ""

    def __init__(self):
        self.neighbors = []
        self.items = []


class Exit(Room):

    def __init__(self):
        super().__init__()


class Dungeon(Location):
    
    def __init__(self):
        super().__init__("Dungeon")
        self._generate()
        self.turn = 0

    # TODO: Use actual procedural systems to generate the dungeon from a seed.
    # The method is hand-coded for now to test the system. Probably use a Strategy pattern for a large variety of dungeons.
    def _generate(self):
        # Create room nodes.
        self.start = Room()
        self.start.description = "This is the starting room of the dungeon.\nThere are doors to the east, north, and west.\nAn exit lies to the south."
        cat_room = Room()
        cat_room.description = "This is a large cavern with all kinds of adorable kitties!\nThere are doors to the west and north."
        lava_room = Room()
        lava_room.description = "There is an unpassable ocean of lava to the north.\nThere are doors to the south and east."
        chess_room = Room()
        chess_room.description = "A variety of chessmen statues occupy a large checkboard floor.\nThe red king is in check.\nThere are doors to the south and west."
        chess_room.items.append(Key("Dragon Key"))
        boss_room = Room()
        boss_room.description = "There is a door to the east."
        boss_room.items.append(Treasure())
        # Create edges between room nodes.
        self.start.neighbors.append(["Go East", cat_room])
        self.start.neighbors.append(["Go North", lava_room])
        self.start.neighbors.append(["Go West", boss_room, "Dragon Key"])
        self.start.neighbors.append(["Exit the Dungeon", Exit()])
        cat_room.neighbors.append(["Go West", self.start])
        cat_room.neighbors.append(["Go North", chess_room])
        lava_room.neighbors.append(["Go South", self.start])
        lava_room.neighbors.append(["Go East", chess_room])
        chess_room.neighbors.append(["Go West", lava_room])
        chess_room.neighbors.append(["Go South", cat_room])
        boss_room.neighbors.append(["Go East", self.start])
        self.current_room = self.start

    def _enter_room(self, system, room):
        self.current_room = room
        if isinstance(self.current_room, Exit):
            self.current_room = self.start
            system.set_location(LocationEnum.TOWN)
            system.print_response("Describe how the player travels back to town.")

    def _item_descriptions(self, room):
        result = ""
        for item in room.items:
            result += f"There is a {item.name}.\n"
        return result

    def _is_locked(self, door) -> bool:
        return len(door) > 2

    def _lock_name(self, door) -> str:
        if len(door) >= 3:
            return door[2]
        return ""

    def _get_room(self, door) -> Room:
        return door[1]

    def get_description(self) -> str:
        return f"{self.current_room.description} \n{self._item_descriptions(self.current_room)}"

    def enter(self):
        self.turn = 0
        self.current_room = self.start

    def get_options(self) -> str:
        result = ""
        i = 0
        for n in self.current_room.neighbors:
            result += f"{i + 1}: {n[0]}\n"
            i += 1
        for item in self.current_room.items:
            result += f"{i + 1}: Take {item.name}\n"
            i += 1
        result += f"{i + 1}: Wait"
        return result

    # TODO: Remove all these silly neighbor list pulls. Use functions to make it actually readable.
    def process_input(self, user_input, system):
        i = user_input - 1
        if i == len(self.current_room.neighbors) + len(self.current_room.items):
            system.print_response("Describe how the player waits for a little bit in only one sentence.")
            self.turn += 1
        elif i < len(self.current_room.neighbors):
            self.turn += 1
            if self._is_locked(self.current_room.neighbors[i]):
                player_keys = system.player.get_keys()
                for key in player_keys:
                    if key.name == self._lock_name(self.current_room.neighbors[i]):
                        self._enter_room(system, self._get_room(self.current_room.neighbors[i]))
                        return
                system.print_response(f"Tell the player that the door is locked in only one sentence. It can only be unlocked with the {self.current_room.neighbors[i][2]}")
            else:
                self._enter_room(system, self._get_room(self.current_room.neighbors[i]))
        elif i < len(self.current_room.neighbors) + len(self.current_room.items):
            i -= len(self.current_room.neighbors)
            item = self.current_room.items.pop(i)
            system.player.take_item(item)
            system.print_response(f"Let the player know that they picked up the {item.name} in only one sentence.")
        else:
            print("Invalid input.")

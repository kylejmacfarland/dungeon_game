import requests
from mob import Player
from util import Time, roll
from datetime import datetime
from location import *
from dungeon import Dungeon
from ai_listener import AiListener

class System:

    locations = {
        LocationEnum.TOWN: Town(), 
        LocationEnum.DUNGEON: Dungeon(), 
    }

    def __init__(self):
        self.current_location = LocationEnum.TOWN
        self.time = Time()
        self.location = Town()
        self.player = Player()
        self.listener = AiListener()

    def _connect_to_server(self, url, model) -> bool:
        if model != "":
            self.listener.model = model
        if url != "":
            print(f"Attempting to connect to {url}")
            response = requests.post(url, json={"model": self.listener.model, "messages": [{"role": "user", "content": "hello"}]}, stream=True)
            if response.status_code == 200:
                self.listener.url = url
                print("Connection succeeded!")
                return True
            else:
                print(f"Connection failed :(\nAttempting to connect to fallback {self.listener.url}")
                response = requests.post(self.listener.url, json={"model": self.listener.model, "messages": [{"role": "user", "content": "hello"}]}, stream=True)
                if response.status_code == 200:
                    print("Connection succeeded!")
                    return True
        else:
            print(f"Attempting to connect to {self.listener.url}")
            response = requests.post(self.listener.url, json={"model": self.listener.model, "messages": [{"role": "user", "content": "hello"}]}, stream=True)
            if response.status_code == 200:
                print("Connection succeeded!")
                return True
        return False


    def _get_int_input(self, prompt) -> int:
        while True:
            user_input = input(prompt)
            try:
                int_value = int(user_input)
                return int_value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def _location(self):
        return self.locations[self.current_location]

    def set_location(self, new_location):
        self.current_location = new_location

    def rest(self) -> int:
        """Rest for one day or until the player is fully healed"""
        self.player.heal(roll(1, 3))
        self.time.next_day()
        days_rested = 1
        while self.player.hp < self.player.max_hp:
            self.player.heal(roll(1, 3))
            self.time.next_day()
            days_rested += 1
        return days_rested

    def print_response(self, message):
        self.listener.request(message + " Keep the response short.")

    def main(self, url="", model=""):
        print("Dungeon Game is Starting...")
        running = True
        if not self._connect_to_server(url, model):
            print("Could not connect to LLM server. Exiting program.")
            return
        self.print_response("Describe the player's quest to enter the dungeon and find the treasure. The player is currently in the town of Oakhaven.")
        while running:
            print("It is " + self.time.get_date() + ". ")
            self.print_response("Describe the current location. " + self._location().get_description())
            print(self._location().get_options())
            user_input = self._get_int_input("> ")
            print("--------------------------------")
            if user_input == 0:
                running = False
                print("Exiting Dungeon Game...")
                self.print_response("Thank the player for playing, and say goodbye!")
            else:
                self._location().process_input(user_input, self)


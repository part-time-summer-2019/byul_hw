from view import View
from model import Model
from model import User_Info
import requests

class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()

    def create_new_user_info(self):
        new_user = self.view.add_user_info()
        self.model.add_user_info(new_user)
    
    def existing_user_info(self): 
        existing_user = self.view.existing_user_info()
        self.model.read_from_userInfo(existing_user)

    def get_user_pokemon(self):
        poke_name = self.view.get_user_pokemon()
        self.model.read_from_pokemon_by_user(poke_name)
    
    def get_user_poke_species(self):
        poke_species = self.view.get_user_species()
        self.model.read_from_poke_species_by_user(poke_species)

    def get_user_poke_habitat(self):
        poke_habitat = self.view.get_user_habitat()
        self.model.read_from_poke_habitat_by_user(poke_habitat)

    def add_pokemon(self): 
        add_poke = self.view.add_pokemon()
        self.model.add_pokemon_info(add_poke)
    
    def delete_user(self):
        remove = self.view.delete_user()
        self.model.delete_user_table(remove)
    

poke = Controller()

##create user
#print(poke.create_new_user_info())

##existing user
#print(poke.existing_user_info())

##create pokemon
# print(poke.add_pokemon())
# print(poke.get_user_pokemon())
print(poke.get_user_poke_species())

from model import User_Info
from model import Pokemon

class View:

    def __init__(self):
        pass
    
    #adding new user info
    def add_user_info(self):
        username = input('Enter your username: ')
        level = input('Enter your pokemon level: ')
        user_summary = User_Info(username, level)
        return user_summary
    
    #add pokemon to user
    def add_pokemon(self):
        username = input('Enter your username: ')
        poke_name = input('Enter pokemon name: ')
        poke_summary = Pokemon(username, poke_name)
        return poke_summary
    
    #viewing existing user info
    def existing_user_info(self):
        username = input('Enter the username you would like to view: ')
        return username
    
    #view user's pokemons
    def get_user_pokemon(self):
        poke_name = input('Enter pokemon name: ')
        return poke_name
    
    #view user's pokemon species
    def get_user_species (self):
        poke_species = input('Enter pokemon species name: ')
        return poke_species
    
    #view user's pokemon habitats
    def get_user_habitat (self):
        poke_habitat = input('Enter pokemon habitat name: ')
        return poke_habitat

    #view user's total pokemon count 
    def poke_count (self):
        get_count = input('How many pokemon does [username] have? (enter username)')
        return get_count

    #delete user information
    def delete_user (self):
        remove_user = input('Enter the username you would like to delete: ')
        return remove_user
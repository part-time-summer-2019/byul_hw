import sqlite3
import requests
import json

#define connection
conn = sqlite3.connect('pokemon_y.db')
c = conn.cursor()

class User_Info:
    def __init__(self, username = None, level = None):
        self.username = username
        self.level = level

class Pokemon: 
    def __init__(self, username = None, poke_name = None):
        self.username = username
        self.poke_name = poke_name

class Model:
    def __init__(self):
        pass

    def add_user_info(self, user_info): #add informaton to the userInfo table
        c.execute("""
            INSERT INTO userInfo (username, level) VALUES (?,?)
            """,
            (user_info.username, user_info.level)
        )
        conn.commit()
        c.close()


    def add_pokemon_info (self, pokeinfo): #add pokemon name to pokemon table
        get_species = requests.get("http://pokeapi.co/api/v2/pokemon/{x}".format(x=pokeinfo.poke_name))
        species_json = get_species.json()
        species = species_json['species']['name'] #get species name[12]

        get_habitat = requests.get("http://pokeapi.co/api/v2/pokemon-species/{x}".format(x=pokeinfo.poke_name))
        habitat_json = get_habitat.json()
        habitat = habitat_json['habitat']['name'] #get habitat name[13]
        c.execute("""
            INSERT INTO pokemon (username, poke_name, species_name, habitat_name) VALUES (?,?,?,?)
            """,
            (pokeinfo.username, pokeinfo.poke_name, species, habitat) 
        )
        conn.commit() #save

        c.execute("""
            INSERT INTO species (poke_name, species_name, habitat_name) VALUES (?,?,?)
            """,
            (pokeinfo.poke_name, species, habitat)

        )
        conn.commit() #save

        c.execute("""
            INSERT INTO habitat (poke_name, poke_habitat, poke_species) VALUES (?,?,?) 
            """,
            (pokeinfo.poke_name, habitat, species)
        )
        conn.commit() #save
        c.close()
    
    def add_pokemon_species (self, species):
        c.execute("""
            INSERT INTO species (poke_name, species_name, habitat_name) VALUES (?,?,?)
            """,
            (species.poke_name, species.species_name, species.habitat_name)
        )
        conn.commit() #save
        c.close()

    
    def add_pokemon_habitat (self, habitat):
        c.execute("""
            INSERT INTO habitat (poke_name, habitat_name, species_name) VALUES (?,?,?)
            """,
            (habitat.poke_name, habitat.habitat_name, habitat.species_name)
        )
        conn.commit() #save
        c.close()

    def read_from_userInfo(self, username): #show userInfo table
        c.execute("SELECT * FROM userInfo")
        [print(row) for row in c.fetchall()]
        conn.commit()
        c.close()
    
    def read_from_pokemon_by_user(self, username):
        c.execute("SELECT poke_name FROM pokemon where poke_name = ?", (username,))
        [print(row) for row in c.fetchall()]
    
    def read_from_poke_species_by_user(self, username):
        c.execute("SELECT species_name FROM pokemon where species_name = ?", (username,))
        [print(row) for row in c.fetchall()]

    def read_from_poke_habitat_by_user(self, username):
        c.execute("SELECT habitat_name FROM pokemon where habit_name = ?", (username,))
        c.execute("SELECT habitat_name FROM pokemon where habit_name = ?", (username,))
        [print(row) for row in c.fetchall()]
  
    def delete_user_table(self, deleteuser): #delete row where username = ?
        c.execute("DELETE FROM userInfo WHERE username = ?", (deleteuser,))
        [print(row) for row in c.fetchall()]
        conn.commit() #save
        c.close()

    def update_user_table(self, change_user): #change username
        c.execute("UPDATE userInfo SET username =? WHERE username ='bcho'", (change_user,))
        [print(row) for row in c.fetchall()]
        conn.commit() #save
        c.close()

    def species_count (self, species):
        c.execute("SELECT COUNT(*) FROM pokemon WHERE species = ?", (species,))
        [print(row) for row in c.fetchall()]
        conn.commit()


#c.close()
#conn.close()



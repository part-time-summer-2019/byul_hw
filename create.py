import sqlite3

conn = sqlite3.connect('pokemon_y.db')

conn.execute(
    """
    CREATE TABLE userInfo(
        id INTEGER PRIMARY KEY,
        username TEXT,
        level TEXT
    );
    """
)
conn.commit()

conn.execute("""
    INSERT INTO userInfo (username, level) VALUES ('zxyz', 'medium');
    """
    )
conn.commit()

conn.execute(
    """
    CREATE TABLE pokemon(
        id INTEGER PRIMARY KEY,
        poke_name TEXT,
        username TEXT,
        species_name TEXT,
        habitat_name TEXT,
        FOREIGN KEY (username) REFERENCES userInfo (username),
        FOREIGN KEY (species_name) REFERENCES species (species_name),
        FOREIGN KEY (habitat_name) REFERENCES habitat (habitat_name)
    );
    """
)
conn.commit()

conn.execute(
    """
    CREATE TABLE species(
        id INTEGER PRIMARY KEY,
        poke_name TEXT,
        species_name TEXT,
        habitat_name TEXT,
        FOREIGN KEY (poke_name) REFERENCES pokemon (poke_name),
        FOREIGN KEY (habitat_name) REFERENCES habitat(habitat_name)
    );
    """
)

conn.execute(
    """
    CREATE TABLE habitat(
        id INTEGER PRIMARY KEY,
        poke_name TEXT,
        poke_species TEXT,
        poke_habitat TEXT,
        FOREIGN KEY (poke_species) REFERENCES species (poke_species),
        FOREIGN KEY (poke_name) REFERENCES pokemon (poke_name)
    );
    """
)

conn.commit()

conn.close()
print("Pokemon Database has been created")
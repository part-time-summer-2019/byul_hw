import sqlite3

conn = sqlite3.connect('bankinfo1.db')

conn.execute(
    """
    CREATE TABLE branch(
        id PRIMARY KEY,
        city TEXT,
        state TEXT,
        zipcode TEXT
    )
    """
)
conn.commit()

conn.execute(
    """
    CREATE TABLE employee(
        id PRIMARY KEY,
        firstname TEXT,
        lastname TEXT,
        empID TEXT,
        salary INT,
        b_id TEXT,
        FOREIGN KEY (b_id) REFERENCES branch (id)
    )
    """
)
conn.commit()


conn.close()


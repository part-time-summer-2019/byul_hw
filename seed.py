import sqlite3
db = 'bankinfo.db'

BLIST=[
    ['Flushing', 'NY', 11368],
    ['Houston', 'TX', 77002]
]

ELIST =[
    ['Lockett', 'Walker', 'S0001', 45000,1],
    ['Coleman', 'Casey', 'S0002', 70000, 1],
    ['Kilome', 'Franklyn', 'S0003', 67000, 1],
    ['Santiago', 'Hector', 'S0004', 10000, 1],
    ['Valdez', 'Framber', 'S0005', 39000, 2],
    ['Peacock', 'Brad', 'S0006', 51000, 2],
    ['Guduan', 'Reymin', 'S0007', 67000, 2],
    ['Cole', 'Gerrit', 'S0008', 55000, 2]
]

conn = sqlite3.connect(db)
c = conn.cursor()

c.execute('DELETE FROM branch')
for branch in BLIST:
    c.execute(
        """
    INSERT INTO branch ('city', 'state', 'zipcode') VALUES (?,?,?)
        """,
    (branch[0], branch[1], branch[2])
    )
conn.commit()

c.execute('DELETE FROM employee')
for employee in ELIST:
    c.execute(
        """
    INSERT INTO employee('firstname', 'lastname', 'empID', 'salary', 'b_id') VALUES (?,?,?,?,?)
        """,
    (employee[0], employee[1], employee[2], employee[3], employee[4])
    )
conn.commit()

print('branch and employee information have been added')

c.close()
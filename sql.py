import sqlite3

conn = sqlite3.connect('bankinfo1.db')



update_sql = "UPDATE employee SET salary=? WHERE empID=?"
conn.execute(update_sql, (73000,'S0007'))
conn.commit()

print('Employees in Flushing Branch')
cursor = conn.execute('SELECT firstname, lastname, empID, salary FROM employee WHERE b_id=1')
for row in cursor:
    print(row)
#     print('First Name: ', row[1])
#     print('Last Name: ', row[0])
#     print('Employee ID: ', row[2])
#     print('Salary: ', row[3])

print()

print('Employees in Houston Branch')
cursor1 = conn.execute('SELECT firstname, lastname, empID, salary FROM employee WHERE b_id=2')
for row in cursor1:
    print(row)
    #print([', '.join(map(str, row)) for row in cursor1])
#     print('First Name: ', row[1])
#     print('Last Name: ', row[0])
#     print('Employee ID: ', row[2])
#     print('Salary: ', row[3])

# print('Done')

conn.close()

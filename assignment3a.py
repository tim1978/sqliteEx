import sqlite3
import random

randNums = []
for i in range(0, 101):
    randNums.append((random.randint(0, 101), ))

with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()

    c.execute("Create Table randNum_t (num Integer)")

    c.executemany("Insert into randNum_t Values(?)", randNums)

    


import sqlite3

conn = sqlite3.connect("newnum.db")
c = conn.cursor()


sql = {'avg': "Select avg(num) from randnum_t",
'max': "Select max(num) from randnum_t",
'min': "Select min(num) from randnum_t",
'sum': "Select sum(num) from randnum_t"}

quit = False
while not quit:
    print "Select one Function by text:"
    print "Avg : avg"
    print "Min : min"
    print "Max : max"
    print "Sum : sum"
    print "quit: q"
    input = raw_input()
    if input.lower() == 'q':
        quit = True

    else:
        c.execute(sql[input.lower()])
        result = c.fetchone()
        print input.lower() + ":", result[0] 

conn.close()


import sqlite3 as sql

con = sql.connect("kahoot_names.db")

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS kahoot_names (name TEXT PRIMARY KEY)''')

mariusnames =  [
"Phil zehole",
"Glouglou Chirac",
"Rezusse léchirst",
"Hue suckwell",
"Husse heukouel",
"Dippin mcthroat",
"G.l.l.o.q.",
"G.2.L.O.Q",
"xX_DaRkS2T",
"Denis molle",
"Hitma ass",
"Musta schkünee",
"Godipim not your mum",
"Milf hunter",
"Book hacké",
"Phil azion",
"Lennybar",
"Hahi menkul",
"Thor pillmoilku",
"James uranus",
"Guess honna",
"Lanar hoods",
"Poe nycook",
"Likmy Cook",
"Pue kinmykunt",
"Jay Dutronc",
"Ethan husse",
"Drill zebut",
"Quentin culle",
"Marie bambelledebit",
"Baveux du vergerons",
"Sacha de Smecta",
"Sacha tpu",
"Sah sha tpu",
"Kuill long",
"Théo fondmabuc",
"Gires hottesamere",
"Yamete ",
"Tim memerde",
"Tim erdeu",
"Peto kask",
"Guy lianal",
"Clitorine",
"Angela Gaulle",
"Angela galle",
"Vianey kitamer",
"Toucherek tal",
"Androm mac",
"Fleur de lautus",
"Jamy lasemence",
"Such happiness",
"Ben Hafoutrh",
"Jamy metzbi1",
"Zouk moidsu",
"Phil stulanal",
"Gourmand",
"Ben Hafoutrh",
"Mahmed Sindouce",
"Hijoui Forbien",
"Ross Putr",
"Kédou Sal",
]

for name in mariusnames:
    cur.execute('''INSERT OR IGNORE INTO kahoot_names VALUES (?)''', (name,))
    con.commit()
    

con.close()

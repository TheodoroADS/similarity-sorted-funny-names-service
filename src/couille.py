from gtts import gTTS
import sqlite3 as sql
import playsound

con = sql.connect("kahoot_names.db")


cur = con.cursor()


cur.execute("SELECT * FROM kahoot_names")


data = cur.fetchall()

data = [jooj[0] for jooj in data]
print(data)

import pygame.mixer
pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")   # chargement de la musique
pygame.mixer.music.play()
# for couille in data:
#     print(couille)
#     gtts = gTTS(couille)
#     gtts.save(couille+".mp3")
#     name=str(couille)+str('.mp3')
#     playsound.playsound(name)

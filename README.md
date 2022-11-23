# Funny Kahoot names database and similarity finder


## What is this?

This project was created many months ago primarily for joke purposes, but it has since fed me a genuine interest in computing similarities between words. This is a (very) small API to upload funny kahoot names to a database, and search for names sorted by similarity to a given string. The idea is to be able to search a funny name that is the closest to the name of the user, or a curse word. For example, "my cock" would return "Mike Hawk" as the most relevant answer. 

## Try it out!

Start the server simply by executing the main.py file: 

``` sh
python3 main.py
```

Open your browser in localhost at the port provided after you run the script and start playing with the web interface!

## API endpoints

GET / : Get a HTML page that serves as an UI interface to access the other routes. 

GET /insert/?name=[the name] : Insert the name provided in the URL query to the names database

POST /insert/ : Insert the name provided in the request's body in the format {"name" : [the name]}

GET /getAll : Gets all of the names inside the database in an array format

GET /get/[the string] : Gets the most similar name to the string passed as a parameter

POST /get/ : Gets the most similar name to the string passed in the request's body in the format {"name" : [the string]}


## About

The technique used is pretty naive, and consists in computing the Levenstein distance the between the phonetic encodings of the provided string and a each name in the database, divided by the length of the longest between the two strings (to avoid penalising longer strings). The name containing the smallest distance is returned. The best performing phonetic encoding algorithm used was soundex. 

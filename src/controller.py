from flask import Blueprint, request
from flask.json import jsonify
from flask import render_template
import sqlite3 as sql
from flask import g
import jellyfish
from . import nameSims
from src.nameSims import levenshteinSim, metaphoneSim, mrcSim, nysiisSym, soundexSim
from jellyfish import jaro_winkler_similarity, metaphone

controller = Blueprint("controller", __name__)

DATABASE = "kahoot_names.db"

nameSet = None

def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sql.connect(DATABASE)
        return db

def loadNames():
    global nameSet
    if nameSet is None:
        print("kiek in de kok")
        # name = request.args['name']
        cur = get_db().cursor()

        cur.execute("SELECT * FROM kahoot_names")

        nameSet = set([name[0] for name in cur.fetchall()])
        return nameSet
    else:
        return nameSet




@controller.route('/', methods = ["GET"])
def homePage():
    return render_template("index.html")


@controller.route('/insert', methods = ['GET','POST'])
def insert():
    if request.method == 'GET':
        name = request.args['name']
    else: #only possibility is that it is post, otherise flask sends bad request error
        name = request.json['suggestion']
        print(name)
    
    if not name:
        print("INSERT: No name w")
        return ("send the fucking name", 406)

    nameset = loadNames()

    if name not in nameset:
            
        con = get_db()
        cur = con.cursor()

        cur.execute(''' INSERT OR IGNORE INTO kahoot_names VALUES (?) ''', (name,))
        con.commit()
        nameset.add(name)


    return ('',204)

@controller.route('/getAll', methods = ['GET'])
def getAll():
    return str(loadNames())

@controller.route('/get', methods = ['POST'])
@controller.route('/get/<name>', methods = ['GET'])
def getSimName(name=None):
    if request.method == 'POST':
        name = request.json['name']
    if name is None:
        return "Send a name"
    return nameSims.closestName(name, loadNames(), soundexSim)
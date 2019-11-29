from flask import Flask, request, render_template, redirect, url_for
import csv
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.Tweet import Tweet, Base 
from  parametrage import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE



engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE))
session = sessionmaker()
session.configure(bind=engine)
s = session()

# Commande pour créer la base de données
Base.metadata.create_all(engine)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue !'

@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
    if request.method == 'POST':

        print(request.form)
        
          dump_to_csv(request.form)

          #Insertion en base de données
          user = request.form["user-name"]
          message =  request.form["user-text"]
          objet_tweet = Tweet(user=user, message=message)
          print(objet_tweet)
          dump_to_db(objet_tweet)

          return redirect(url_for('timeline'))
        
        
        #return "OK"
    if request.method == 'GET':
        return render_template('formulaire.html')



@app.route('/timeline', methods=['GET'])
def timeline():
    gaz = parse_from_csv()
    gaz_db = parse_from_db()
    return render_template("timeline.html", gaz = gaz, gaz_db = gaz_db)

def parse_from_csv():
    gaz = []
    with open('./gazouilles.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row[1]) <= 280:
                gaz.append({"user":row[0], "text":row[1]})
    return gaz

def parse_from_db():
  gaz =[]
  for p in s.query(Tweet).all():
    gaz.append({"user":p.user, "text":p.message})


def dump_to_csv(d):
	donnees = [d["user-name"],d["user-text"] ]
	with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
    print(d)
   
    donnees = [d["user-name"],d["user-text"] ]
    with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
      writer = csv.writer(f)
      writer.writerow(donnees)

def dump_to_db(tweet):
    print(tweet)
    s.add(tweet)
    s.commit()

@app.route('/timeline/<name>/', methods=['GET'])
def get_timeline(name):
    print(name)
    gaz = get_timeline_user_from_csv(name)
    gaz_db = get_timeline_user_from_csv(name)
    return render_template("timeline.html", gaz = gaz, gaz_db = gaz_db)

def get_timeline_user_from_csv(name):
  """
    function get_timeline_user: 
    param1 : nom d'utilisateur (String)

    retourne une listes de tweet d'un utisateur
  function get_timeline_user: recupere la liste de tweet d'un utilisateur 
  Parameters
  ----------
  user: string
  nom de l'utilisateur

  Return
  -------
  string
  liste de tweet d'un utilisateur

  """
  gaz = []    
  with open('./gazouilles.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
      if row[0] == name:
        gaz.append({"user":row[0], "text":row[1]})
  return gaz


  def get_timeline_user_from_db(name):
    """
    function get_timeline_user_from_db: 
    param1 : nom d'utilisateur (String)

    retourne une listes de tweet d'un utisateur
    function get_timeline_user: recupere la liste de tweet d'un utilisateur 
    Parameters
    ----------
    user: string
    nom de l'utilisateur

    Return
    -------
    string
    liste de tweet d'un utilisateur

    """
    gaz = []

    for p in s.query(Tweet).filter_by(user=name):
      gaz.append({"user":p.user, "text":p.message})  
    return gaz

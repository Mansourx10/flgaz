from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue !'

@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
	if request.method == 'POST':
		print(request.form)
		if len(request.form["user-name"]) < 20 and len(request.form["user-text"]) <= 280:
		    dump_to_csv(request.form)
		    return redirect(url_for('timeline'))
		  #return "OK"
		else:
		    return "message trop long"

	if request.method == 'GET':
		return render_template('formulaire.html')

@app.route('/timeline', methods=['GET'])
def timeline():
	gaz = parse_from_csv()
	return render_template("timeline.html", gaz = gaz)

def parse_from_csv():
	gaz = []
	with open('./gazouilles.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
		    if len(row[1]) <= 280:
		        gaz.append({"user":row[0], "text":row[1]})
	return gaz

def dump_to_csv(d):
	donnees = [d["user-name"],d["user-text"] ]
	with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(donnees)

@app.route('/timeline/<name>/', methods=['GET'])
def get_timeline(name):
    print(name)
    gaz = get_timeline_user(name)
    return render_template("timeline.html", gaz = gaz)

def get_timeline_user(name):
    gaz = []
    with open('./gazouilles.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == name:
                gaz.append({"user":row[0], "text":row[1]})
    return gaz
import flask
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = flask.Flask(__name__, template_folder='api-pages')
app.secret_key = os.urandom(12)
app.config["DEBUG"] = True

clientId = ""


def get_db_connection():
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    return db


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('user_page.html')


@app.route('/login', methods=['POST'])
def do_login():
    conn = get_db_connection()
    user = conn.execute(
        f'SELECT id, adresse_mail , password FROM client WHERE adresse_mail=="{request.form["email"]}" AND password=="{request.form["password"]}"').fetchone()
    conn.close()
    if user is not None:
        global clientId
        clientId = user["id"]
        print(clientId)
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    global clientId
    clientId = ""
    return home()


@app.route("/fly")
def fly():
    conn = get_db_connection()
    fly_list = conn.execute('SELECT * FROM vol').fetchall()
    conn.close()
    return render_template('fly.html', flylist=fly_list)


@app.route("/reservation")
def reservation():
    conn = get_db_connection()
    reservation_list = conn.execute(f'SELECT * FROM reservation WHERE id_client=="{clientId}"').fetchall()
    conn.close()
    return render_template('reservation.html',reslist=reservation_list)


@app.route("/reserved",  methods=['POST'])
def reserved():
    print(request.form["id"])
    connGet = get_db_connection()
    vol = connGet.execute(f'SELECT id,date,heure_départ,heure_arrivée,lieu_départ,destination,prix FROM vol WHERE id=="{request.form["id"]}"').fetchone()
    connGet.close()
    connInsert = get_db_connection()
    connInsert.execute(f"""INSERT INTO reservation(id_vol,id_client,date,destination,lieu_départ,prix) VALUES (?,?,?,?,?,?)""",
                       (vol["id"],clientId,vol["date"],vol["destination"],vol["lieu_départ"],vol["prix"]))
    connInsert.commit()
    connInsert.close()
    return render_template('reserved.html',vol=vol)


@app.route("/about")
def about():
    conn = get_db_connection()
    user = conn.execute(f'SELECT * FROM client WHERE id=="{clientId}"').fetchone()
    conn.close()
    return render_template('about.html', user=user)

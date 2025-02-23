from flask import Flask
import sqlite3
from flask import request
from datetime import datetime

app = Flask(__name__)

"""Anmeldung() speichert die eMail-Adressen mit einem Zeitstempel in der DB, falls
   diese nicht schon vorhanden sind, und gibt die Anzahl der DB-Einträge zurück"""

def Anmeldung(): 
    conn = sqlite3.connect('Anmeldungen.db')
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM Anmeldungen')
    i = len(cursor.fetchall())
    conn.close()
    if request.method == 'POST': 
        email = request.form['email']
        zeit = str(datetime.now()) 
        conn = sqlite3.connect('Anmeldungen.db')
        cursor = conn.cursor()
        cursor.execute('SELECT email FROM Anmeldungen')
        rows = cursor.fetchall()
        i = len(rows)
        if any(email in s for s in rows):
            return i
        else: 
            cursor.execute('INSERT INTO Anmeldungen (email, Zeit) VALUES (?,?)', (email, zeit))
            conn.commit() 
            conn.close()
            i += 1
            return i
    return i  
           

"""Schnittstelle für das Frontend""" 

@app.route("/", methods=['GET', 'POST'])
def Frontend(): 
    i = Anmeldung() 
    return '''
<html>
    <body>
    <center>
     <div style = "margin-top: 10%">
     <h1>Anmeldung</h1>
     <p>Wenn Sie Interesse an unserem Produkt haben und mit uns in Kontakt treten wollen,<br>
       können Sie sich hier anmelden, indem Sie ihre E-Mail-Adresse hinterlassen. </p> 
       <p> Es haben sich bisher ''' + str(i) + ''' Personen bei uns angemeldet. </p> <br>
        <form action = "https://fstring-anmeldung.azurewebsites.net", method = "POST">
        <label for="email">E-Mail-Adresse:</label>
        <input type="text" name="email" pattern="[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"><br><br>
        <input type="submit" value="Anmelden">
        </form>
     </div>
    </body>
</html>'''

"""Admin-Zugriff"""
@app.route("/registrations", methods=['GET'])
def AlleAnmeldungen(): 
    conn = sqlite3.connect('Anmeldungen.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Anmeldungen')
    rows = cursor.fetchall()
    conn.commit() 
    conn.close()
    return str(rows) 



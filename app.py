from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET'])
def Frontend(): 
    return '''
<html>
    <body>
    <center>
     <div style = "margin-top: 10%">
     <h1>Anmeldung</h1>
     <p>Wenn Sie Interesse an unserem Produkt haben und mit uns in Kontakt treten wollen,<br>
       können Sie sich hier anmelden, indem Sie ihre eMail-Adresse hinterlassen. </p> 
       <p> Es haben sich bisher X Personen bei uns angemeldet. </p> <br>
        <form action = "http://127.0.0.1:5000/Anmeldung", method = "POST">
        <label for="email">eMail-Adresse:</label>
        <input type="text" name="email"><br><br>
        <input type="submit" value="Anmelden">
        </form>
     </div>
    </body>
</html>'''

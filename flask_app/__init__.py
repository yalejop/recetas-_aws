from flask import Flask

app = Flask(__name__)

#generar la secret_key
app.secret_key ='Esta es mi llave secreta'
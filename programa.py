from flask import *
from flask_sqlalchemy import *

app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///estudiantes.sqlite3"

db=SQLAlchemy(app);

class Estudiante(db.Model):
    id=db.Column('id_estudiante',db.Integer,primary_key=True)

    nombre=db.Column(db.String(50))
    codigo=db.Column(db.String(12))

    def __init__(self, nombre, codigo):
        self.nombre=nombre
        self.codigo=codigo


@app.route('/')
def bienvenida():
    return render_template("Bienvenida.html")


with app.app_context():

    db.create_all()
    app.run(debug=True)


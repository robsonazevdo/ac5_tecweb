from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Projetoac5.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(10), unique=True, nullable=False)
    sobrenome = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(35), unique=True, nullable=False)
    assunto = db.Column(db.String(15), unique=True, nullable=False)
    hora = db.Column(db.DateTime, default=datetime.now)
    mensagem = db.Column(db.String(150), unique=True, nullable=False)

    db.create_all()

@app.route("/contato")
@app.route('/')
def contato():
    return  render_template('login.html')

@app.route('/api/seus_dados', methods=['GET','POST'])
def seus_dados():




@app.route("/obrigado")
@app.route('/')
def obrigado():
    return  render_template('obrigado.html')



if __name__ == '__main__':
    app.run(debug=True)

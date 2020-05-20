from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Projetoac5.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contato(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(10), nullable=True)
    sobrenome = db.Column(db.String(25), nullable=True)
    email = db.Column(db.String(35), nullable=True)
    assunto = db.Column(db.String(15), nullable=True)
    hora = db.Column(db.DateTime, default=datetime.now)
    mensagem = db.Column(db.String(150),nullable=True)

    db.create_all()

@app.route("/contato")
@app.route('/')
def contato():
    return  render_template('login.html')


@app.route('/seus_dados', methods=['GET','POST'])
def seus_dados():
    if request.method == 'POST':
        print(request.form['nome'])

        usuario = Contato(nome=request.form['nome'], sobrenome=request.form['sobrenome'], 
                          email=request.form['email'], assunto=request.form['assunto'], 
                          mensagem=request.form['mensagem'])
        db.session.add(usuario)
        db.session.commit()

        return  render_template('obrigado.html')


@app.route("/obrigado")
@app.route('/')
def obrigado():
    return  render_template('obrigado.html')



if __name__ == '__main__':
    app.run(debug=True)

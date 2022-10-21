from random import randint

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    valor = "Jogo de adivinhar o número"

    if request.method == "GET":
        return render_template('index.html', valor=valor)
    else:
        num = randint(1, 10)
        palpite = int(request.form.get("name"))
        if num == palpite:
            return '<h1>Parabéns, você acertou!</h1>'
        else:
            return '<h1>Que pena, você errou!</h1>'


@app.route('/sobre')
def sobre():
    return "<h1>Sobre</h1>"


@app.route('/<string:nome>')
def NotFound(nome):
    varialvel = f"Página ({nome}) não existe"
    return render_template("error.html", variavel=varialvel)


app.run(debug=True)

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
            return '<h1>Que pena, você errou!<br>O número era ({})</h1>'.format(num)


@app.route('/button')
def button():
    return render_template('button.html')


@app.route('/on', methods=["POST"])
def on():
    msgON = "Ligado"
    return render_template('on.html', msgON=msgON)


@app.route('/off', methods=["POST"])
def off():
    msgOFF = "Desligado"
    return render_template('off.html', msgOFF=msgOFF)


@app.route('/<string:nome>')
def NotFound(nome):
    variavel = f"Página ({nome}) não existe"
    return render_template("error.html", variavel=variavel)


app.run(debug=True)

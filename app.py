from flask import Flask, render_template, request, flash, Response
from contador import contador_palabras

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def index():


    if (request.method == 'POST'):
        sms = request.form.get('pregunta')
        frase = contador_palabras(sms)

        return render_template("respuesta.html", frase=frase)
        
    else:
        print('No entro')


    return render_template("index.html")


@app.route('/resp', methods=["GET","POST"])
def respuesta():

    return render_template("respuesta.html")


# app run
if __name__ == "__main__":
    app.run(debug=True)
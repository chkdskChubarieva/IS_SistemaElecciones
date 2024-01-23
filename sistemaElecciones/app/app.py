from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    numeros_dia = range(1 , 32)
    meses = ['1 - Enero', '2 - Febrero', '3 - Marzo', '4 - Abril', '5 - Mayo',
             '6 - Junio', '7 - Julio', '8 - Agosto', '9 - Septiembre', '10 - Octubre',
             '11 - Noviembre', '12 - Diciembre']
    return render_template(
        'index.html', numeros_dia=numeros_dia, meses=meses
        )

if __name__ == '__main__':
    app.run(debug=True, port=5000)

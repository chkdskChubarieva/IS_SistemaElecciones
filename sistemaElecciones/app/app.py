from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
# Conexión MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'base_datos'

conexion = MySQL(app)


@app.route('/')

def index():
    numeros_dia = range(1 , 32)
    meses = ['1 - Enero', '2 - Febrero', '3 - Marzo', '4 - Abril', '5 - Mayo',
             '6 - Junio', '7 - Julio', '8 - Agosto', '9 - Septiembre', '10 - Octubre',
             '11 - Noviembre', '12 - Diciembre']
    ci = [7913557, 3234543, 3758493, 9384756]
    fecha_nac = ['2000-01-23', '1990-04-17', '1997-05-10', '2001-12-07'] 
    return render_template('index.html', numeros_dia=numeros_dia, meses=meses)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import config
# Modelos:
from models.ModeloElector import ModeloElector

# Entidades:
from models.entities.elector import Elector
from models.entities.candidato import Candidato
from models.entities.voto import Voto
app = Flask(__name__)

app.secret_key = 'mundolibre'

conexion = MySQL(app)
login_manager_app = LoginManager(app)




@login_manager_app.user_loader
def load_user(ci):
    return ModeloElector.get_by_id(conexion, ci)

@app.route('/')

def index():
   
    return redirect(url_for('login'))

@app.route('/login')
def diccionario():
    numeros_dia = range(1 , 32)
    meses = ['1 - Enero', '2 - Febrero', '3 - Marzo', '4 - Abril', '5 - Mayo',
             '6 - Junio', '7 - Julio', '8 - Agosto', '9 - Septiembre', '10 - Octubre',
             '11 - Noviembre', '12 - Diciembre']
    cadena_anios = range(1950 ,2010)
    anios = cadena_anios[::-1]
    
    return render_template('login.html', numeros_dia=numeros_dia, meses=meses, anios=anios)
    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    

    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        
        dia = request.form.get('dia') # recupera ci del formulario
        mes = request.form.get('month')
        partes = mes.split('-')
        valor_mes = partes[0].strip()
        anio = request.form.get('anio')
        fecha_n = anio + "-" + valor_mes +"-"+dia
        global logged_user
        elector = Elector('name', request.form['ci'], fecha_n, 1, 'genero')
        logged_user = ModeloElector.login(conexion, elector)
        if logged_user != None:
            if logged_user.habilitado == 1:
                login_user(logged_user)
                return redirect(url_for('verDatos'))
            else:
                flash("Está inhabilitado para votar")
                return redirect(url_for('login'))
        else:
            flash("No está registrado en el padrón electoral")
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
 
@app.route('/verDatos')
@login_required
def verDatos():
    return render_template('/verDatos.html')   
  



@app.route('/emitirVoto') 
@login_required
def emitir():
    candidato1 = Candidato('javier milei',97, '1990-10-01', 'Masculino','KML')
    candidato2 = Candidato('sergio massa',98,'1990-11-01', 'Masculino', 'XYZ')
    candidato3 = Candidato('patricia bullrich', 99, '1990-12-01', 'Femenino', 'RQT')
    candidatos=[candidato1, candidato2, candidato3]
   
    return render_template('/emitirVoto.html', candidatos=candidatos) 
votos =[]
@app.route('/emitirVoto', methods=['GET', 'POST']) 
@login_required
def emitirVoto():
   global logged_user
   if request.method == 'POST':
    voto = Voto(logged_user, request.form.get('voto'))
    votos.append(voto)
    ModeloElector.votar(conexion, logged_user)
    flash("Tú {} Has votado por:{} tu estado es {}".format(logged_user.nombre,request.form.get('voto'), logged_user.habilitado))
    return redirect(url_for('resultados'))

@app.route('/resultados') 
@login_required
def resultados():
    contador_votos_cand1 = 0
    contador_votos_cand2 = 0
    contador_votos_cand3 = 0
    for voto in votos:
        if voto.voto == 'KML':
            contador_votos_cand1 +=1
        if voto.voto == 'XYZ':
            contador_votos_cand2 +=1
        if voto.voto == 'RQT':
            contador_votos_cand3 +=1
    return render_template('resultados.html', contador1=contador_votos_cand1, contador2=contador_votos_cand2, contador3=contador_votos_cand3)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/verDatos')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404
    
if __name__ == '__main__':
        app.config.from_object(config['development'])
        app.register_error_handler(401, status_401)
        app.register_error_handler(404, status_404)
        app.run()
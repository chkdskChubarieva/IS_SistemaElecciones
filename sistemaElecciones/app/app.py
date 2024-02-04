from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin


app = Flask(__name__)

app.secret_key = 'mundolibre'
login_manager_app = LoginManager(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:mundolibre@localhost/chkdsk7$sistemaelecciones'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
conexion = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#@login_manager_app.user_loader
#def load_user(user_id):
#    return Elector.query.get(int(user_id))


class Elector(conexion.Model, UserMixin):
    ID_ELECTOR = conexion.Column(conexion.Integer, primary_key=True, autoincrement=True)
    NOMBRE = conexion.Column(conexion.String(30))
    CI = conexion.Column(conexion.String(10))
    FECHA_NACIMIENTO = conexion.Column(conexion.Date)
    GENERO = conexion.Column(conexion.String(15))
    ESTADO_HABILITADO = conexion.Column(conexion.Integer)

    def get_id(self):
        return str(self.ID_ELECTOR)
    
class Candidato(conexion.Model): #nombre, ci, fecha_nacimiento, genero, partido
    ID_CANDIDATO = conexion.Column(conexion.Integer, primary_key=True, autoincrement=True)
    NOMBRE = conexion.Column(conexion.String(30))
    CI = conexion.Column(conexion.String(10))
    FECHA_NACIMIENTO = conexion.Column(conexion.Date)
    GENERO = conexion.Column(conexion.String(15))
    votos = conexion.Column(conexion.Integer)
    FOTO = conexion.Column(conexion.String(50))
    PARTIDO = conexion.Column(conexion.String(20))   
    

class Comite(conexion.Model, UserMixin):
    COD_COMITE = conexion.Column(conexion.String(15), primary_key=True)
    NOMBRE = conexion.Column(conexion.String(30))
    CI = conexion.Column(conexion.String(10))
    FECHA_NACIMIENTO = conexion.Column(conexion.Date)
    GENERO = conexion.Column(conexion.String(15))
    ROL = conexion.Column(conexion.String(15))
    def get_id(self):
        return str(self.CI)

#users = {
   # 'elector_user': Elector('elector_user'),
   # 'comite_user': Comite('comite_user')
#}
@login_manager.user_loader
def load_user(user_id):
        return Elector.query.get(int(user_id))
  

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
        logged_user = Elector.query.filter_by(CI=request.form['ci'], FECHA_NACIMIENTO=fecha_n).first()
       
        if logged_user != None:
            if logged_user.ESTADO_HABILITADO == 1:
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
   
    candidatos=Candidato.query.all()
    return render_template('/emitirVoto.html', candidatos=candidatos) 

@app.route('/emitirVoto', methods=['GET', 'POST']) 
@login_required
def emitirVoto():
    #voto = Voto(logged_user, request.form.get('voto'))
   global logged_user
   if request.method == 'POST':
    candidato = Candidato.query.filter_by(PARTIDO=request.form.get('voto')).first()
    if candidato:
        # Aumenta en uno el valor de los votos del candidato
        candidato.votos += 1
        # Guarda los cambios en la base de datos
       
        #Elector.query.filter_by(CI=logged_user.CI).update({'ESTADO_HABILITADO': '0'})

        # Confirma los cambios en la base de datos
        conexion.session.commit()
        
        flash("Has votado por:{}".format(candidato.NOMBRE))
    else:
        print("No se encontró ningún candidato")
    
    return redirect(url_for('logout'))

@app.route('/resultados')

def resultados():
    cantidad_votos=0
    candidatos=Candidato.query.all()
    for candidato in candidatos:
        cantidad_votos += candidato.votos
        
    return render_template('resultados.html', candidatos=candidatos, cantidad_votos=cantidad_votos)

@app.route('/login_comite')
def login_c():
    return render_template('/login_comite.html')

@app.route('/login_comite', methods=['GET', 'POST'])
def login_comite():
    if request.method == 'POST':
        global logged_comite
        logged_comite = Comite.query.filter_by(CI=request.form['ci'], COD_COMITE=request.form['codigo_comite']).first()
        if logged_comite != None:
            login_user(logged_comite)
            return redirect(url_for('resultados'))
        else:
            flash("No está registrado como miembro del comite electoral")
            return redirect(url_for('login_comite'))
    else:
        return redirect(url_for('login_comite'))
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404
    
if __name__ == '__main__':
        #app.config.from_object(config['development'])
        app.register_error_handler(401, status_401)
        app.register_error_handler(404, status_404)
        app.run(debug=True, port=5000)
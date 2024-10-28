import os
from flask import Flask
#from config import app,db
from routes.aluno_routes import alunos_bp
from routes.professor_routes import professores_bp
from routes.turma_routes import turmas_bp


app = Flask(__name__)
app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)


#with app.app_context():
    #db.create_all()

if __name__ == '__main__':
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", "True").lower() == "true"
    
    app.run(host=host, port=port, debug=debug)
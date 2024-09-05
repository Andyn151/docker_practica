from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión SQLAlchemy
db = SQLAlchemy(app)

# Ejemplo de un modelo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Rutas y lógica de la aplicación
@app.route('/counter', methods=['GET'])
def get_counter():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8500)


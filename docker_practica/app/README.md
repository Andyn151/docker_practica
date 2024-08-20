# Flask PostgreSQL Microservice

## Descripción de la aplicación
Esta aplicación es un microservicio que permite leer y escribir datos en una base de datos PostgreSQL.

## Funcionamiento de la aplicación
La aplicación expone dos endpoints:
- `GET /counter`: Devuelve el valor actual del contador.
- `POST /counter`: Incrementa el contador y devuelve el nuevo valor.

## Requisitos
- Docker y Docker Compose

## Instrucciones para ejecutarla en local
1. Clonar el repositorio.
2. Construir y ejecutar los contenedores usando Docker Compose:
   ```sh
   docker-compose up --build

Crear fichero README.md


## Implementar la aplicación

1. Crea una carpeta llamada `app` dentro de tu repositorio.
2. Dentro de la carpeta `app`, crea un archivo `app.py` con el siguiente contenido:

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

## Crea un archivo requirements.txt dentro de la carpeta app con las dependencias necesarias:

flask==2.3.2
flask-SQLAlchemy==3.0.0
SQLAlchemy==1.4.41


## Dentro de la carpeta app, crea un archivo Dockerfile con el siguiente contenido:

# Etapa de construcción
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Etapa final
FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .

CMD ["python", "app.py"]

## En la raíz del repositorio, crea un archivo docker-compose.yml con el siguiente contenido:

version: '3.9'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: flaskdb
    volumes:
      - postgres-data:/var/lib/postgresql/data

  web:
    build: ./app
    ports:
      - "8500:5000"  # Puerto local 8500 redirige al puerto 5000 dentro del contenedor
    environment:
      DB_HOST: db
      DB_PORT: 5432
      DB_USER: postgres
      DB_PASSWORD: postgres
      DB_NAME: flaskdb
    depends_on:
      - db

volumes:
  postgres-data:

## Construye y ejecuta los contenedores usando Docker Compose:

docker compose up --build
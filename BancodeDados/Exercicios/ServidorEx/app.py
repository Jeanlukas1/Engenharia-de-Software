from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DB_NAME = "exerciciodeconexaodebanco"
DB_USER = "postgres"
DB_PASSWORD = "1907050603Jl@"
DB_HOST = "localhost"

# objetivo de conectar com o banco de dados
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )

@app.route('/aluno', methods=['POST'])
def add_aluno():
    data = request.get_json()
    nome = data.get('nome')
    idade = data.get('idade')
    curso = data.get('curso')

    # BAD REQUEST
    if not nome or not idade or not curso:
        return jsonify({'error': 'Dados incompletos'}), 400

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)", (nome, int(idade), curso))
        conn.commit()
        return jsonify({'message': 'Aluno inserido com sucesso'}), 200
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:
            cur.close()
            conn.close()

@app.route('/alunos', methods=['GET'])
def get_alunos():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM alunos")
        alunos = cur.fetchall()
        return jsonify(alunos)
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:
            cur.close()
            conn.close()

@app.route('/professor', methods=['POST'])
def add_professor():
    data = request.get_json()
    nome = data.get('nome')
    disciplina = data.get('disciplina')

    if not nome or not disciplina:
        return jsonify({'error': 'Dados incompletos'}), 400

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO professores (nome, disciplina) VALUES (%s, %s)", (nome, disciplina))
        conn.commit()
        return jsonify({'message': 'Professor inserido com sucesso'}), 201
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:
            cur.close()
            conn.close()

@app.route('/professores', methods=['GET'])
def get_professores():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM professores")
        professores = cur.fetchall()
        return jsonify(professores)
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)

# Para inserir aluno:
#curl -X POST http://127.0.0.1:5000/alunos -H "Content-Type: application/json" -d "{\"nome\":\"João Silva\", \"idade\":21, \"curso\":\"Engenharia\"}"

#Listar Alunos
# curl http://127.0.0.1:5000/alunos

# Inserir professor
# curl -X POST http://127.0.0.1:5000/professores -H "Content-Type: application/json" -d "{\"nome\":\"Maria Souza\", \"disciplina\":\"Matemática\"}"

#Listar professor
#curl http://127.0.0.1:5000/professores

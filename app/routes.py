from flask import render_template, request, redirect
from app import app, get_db_connection

@app.route('/')
def index():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
    connection.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/add', methods=['POST'])
def add_user():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['pass']
    
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
        connection.commit()
    connection.close()
    return redirect('/')

@app.route('/login', methods=['POST', 'GET'])
def login():
    pass 
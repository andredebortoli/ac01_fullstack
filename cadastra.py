import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)

#MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'andre2604'
app.config['MYSQL_DATABASE-DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)




@app.route('/')
def main():
    return render_template('cadastro.html')



@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    endereco = request.form['endereco']

    if nome and cpf and endereco:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tb_user (nome, cpf, endereco) VALUES (%s, %s, %s)', (nome, cpf, endereco))
        conn.commit()
    return render_template('cadastro.html')



@app.route('/listar', methods=['POST', 'GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select nome, cpf, endereco from tb_user')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    data_nascimento = request.form['data-nascimento']
    cpf = request.form['cpf']
    password = request.form['password']
    genero = request.form['genero']
    email = request.form.get('email')  # use get to handle optional fields
    telefone = request.form.get('telefone')  # use get to handle optional fields

    # Aqui você pode processar e armazenar os dados, por exemplo, em um banco de dados
    return (f'''Nome: {nome}<br>
            Sobrenome: {sobrenome}<br>
            Data de Nascimento: {data_nascimento}<br>
            CPF: {cpf}<br>
            Gênero: {genero}<br>
            Email: {email}<br>
            Telefone: {telefone}''')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    data_nascimento = request.form['data-nascimento']
    cpf = request.form['cpf']
    password = request.form['password']
    genero = request.form['genero']
    email = request.form.get('email')
    telefone = request.form.get('telefone')

    return index() if nome.isalpha() else form()

if __name__ == '__main__':
    app.run(debug=True)


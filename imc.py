from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') #Definição de rota (Neste caso a rota raiz.)
def index(): # Função de nome index
    return render_template('home.html') #Conteúdo da rota

@app.route("/calcular_imc_get")#por padrão é get,  methods=['GET'] não é necessário pois por padrão todas as requisições no flask são GET
def calcular_imc_get():
    args = request.args
    altura = float( args.get('txt_altura'))
    peso = float( args.get('txt_peso'))
    imc = peso / (altura * altura)
    if imc < 18.5:
        classificacao = 'MAGREZA'
    elif 18.5 <= imc <= 24.9:
        classificacao = 'NORMAL'
    elif 25 <= imc <= 29.9:
        classificacao = 'SOBREPESO'
    elif 30 <= imc <= 39.9:
        classificacao = 'OBESIDADE'
    else:
        classificacao = 'OBESIDADE GRAVE'
    return render_template('home.html') #deixei somente como post para exibir resultado somente no post

@app.route('/calcular_imc', methods=['POST'])
def calc_imc():
    altura = float(request.form['txt_altura'])
    peso = float(request.form['txt_peso'])
    imc = peso / (altura * altura)

    if imc < 18.5:
        classificacao = 'MAGREZA'
    elif 18.5 <= imc <= 24.9:
        classificacao = 'NORMAL'
    elif 25 <= imc <= 29.9:
        classificacao = 'SOBREPESO'
    elif 30 <= imc <= 39.9:
        classificacao = 'OBESIDADE'
    else:
        classificacao = 'OBESIDADE GRAVE'
    return render_template('home.html', res_imc = f'{imc:.2f}', res_classificacao = classificacao)


if __name__ == "__main__": #excecuta essa linha executando direto do código, se for importado por outro não.
    app.run(debug=True) #debug=True serve para ativar o debugar do sistema, ele salva automáticamente 
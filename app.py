from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_patrimonio(investimento_mensal, anos, rendimento_mensal):
    meses = anos * 12
    patrimonio = 0
    for _ in range(meses):
        patrimonio = (patrimonio + investimento_mensal) * (1 + rendimento_mensal)
    return patrimonio

def calcular_dividendos(patrimonio, taxa_dividendos=0.008):  # 0.8% ao mês
    return patrimonio * taxa_dividendos

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        investimento = float(request.form['investimento'])
        anos = int(request.form['anos'])
        rendimento = float(request.form['rendimento']) / 100

        patrimonio = calcular_patrimonio(investimento, anos, rendimento)
        dividendos = calcular_dividendos(patrimonio)

        resultado = {
            'patrimonio': f"R$ {patrimonio:,.2f}",
            'dividendos': f"R$ {dividendos:,.2f}"
        }

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
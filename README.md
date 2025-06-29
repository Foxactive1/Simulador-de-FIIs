# 📈 Simulador de Investimento em FIIs

Simples aplicação web desenvolvida com **Python + Flask** que permite simular aportes mensais em **Fundos Imobiliários (FIIs)**, exibindo ao final o **patrimônio acumulado** e os **dividendos mensais estimados** com base na taxa de rendimento informada.

---

## 🚀 Funcionalidades

- 💰 Simular investimento mensal ao longo dos anos
- 📊 Calcular patrimônio final com juros compostos
- 📈 Estimar dividendos mensais com base no patrimônio final
- 🖥️ Interface web amigável (HTML + Bootstrap)

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)

---

## 💻 Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/simulador-fiis-flask.git
cd simulador-fiis-flask

2. Crie um ambiente virtual (opcional, mas recomendado)

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências

pip install flask

4. Execute o aplicativo

python app.py

Acesse no navegador: http://localhost:5000


---

🧮 Fórmulas Utilizadas

Cálculo do patrimônio acumulado:

patrimonio = (patrimonio + aporte_mensal) * (1 + rendimento_mensal)

Cálculo dos dividendos mensais:

dividendos = patrimonio * taxa_dividendos


> 🔁 A simulação considera aportes mensais constantes e rendimento composto.

📌 Exemplo de Uso

1. Informe quanto deseja investir por mês


2. Defina o número de anos do investimento


3. Insira a taxa média de rendimento mensal esperada


4. Clique em Calcular


5. Veja o patrimônio acumulado e os dividendos mensais estimados 💸


📂 Estrutura do Projeto

simulador_fiis/
├── app.py
└── templates/
    └── index.html

📅 Roadmap (Melhorias Futuras)

[ ] Exportar relatório para PDF

[ ] Adicionar gráficos de evolução do patrimônio

[ ] Salvar histórico de simulações

[ ] Integração com dados reais (ex: B3 ou StatusInvest)

[ ] Interface com autenticação de usuários

📃 Licença

Distribuído sob a licença MIT. Veja LICENSE para mais informações.

👨‍💻 Autor

Desenvolvido por Dione Castro Alves — InNovaIdeia Assessoria em Tecnologia

🏷️ Hashtags (para LinkedIn ou divulgação)

#FIIs #Investimentos #Flask #Python #JurosCompostos #SimuladorFinanceiro #Inovação #FinançasPessoais #InNovaIdeia #OpenSource



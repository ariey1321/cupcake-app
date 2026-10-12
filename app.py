from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Model: Simulação de dados do banco de dados (Cupcakes)
def obter_cupcakes_banco():
    return [
        {"id": 1, "nome": "Red Velvet Gourmet", "sabor": "Cream Cheese", "preco": 12.50},
        {"id": 2, "nome": "ChocoNinho Supremo", "sabor": "Leite Ninho", "preco": 14.00},
        {"id": 3, "nome": "Sensação Morango", "sabor": "Morango com Chocolate", "preco": 11.00}
    ]

# Controller: Rotas da Aplicação
@app.route('/')
def home():
    # Retorna a View (Interface)
    return render_template('index.html')

@app.route('/api/cupcakes', methods=['GET'])
def listar_cupcakes():
    # Retorna a lista de produtos em formato JSON
    cupcakes = obter_cupcakes_banco()
    return jsonify(cupcakes)

if __name__ == '__main__':
    print("Servidor da Loja de Cupcakes rodando na porta 5000...")
    app.run(debug=True)
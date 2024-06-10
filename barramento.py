from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Importação do CORS

app = Flask(__name__)
CORS(app)  # Ativação do CORS para todas as rotas

BACKEND_URL = 'http://localhost:5000'

# Rota para registro
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        response = requests.post(f'{BACKEND_URL}/register', json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

# Rota para login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        response = requests.post(f'{BACKEND_URL}/login', json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

# Rota para obter as vagas ativas
@app.route('/active_spot', methods=['POST'])
def get_active_spot():
    data = request.get_json()
    placa_do_carro = data.get('placaDoCarro')
    if not placa_do_carro:
        return jsonify({'message': 'Placa do carro não fornecida.'}), 400
    try:
        response = requests.post(f'{BACKEND_URL}/active_spot', json={'placaDoCarro': placa_do_carro})
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

# Rota para obter todos os clientes
@app.route('/clientes', methods=['GET'])
def get_all_clientes():
    try:
        response = requests.get(f'{BACKEND_URL}/clientes')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)

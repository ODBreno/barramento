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

@app.route('/login_fiscal', methods=['POST'])
def login_fiscal():
    data = request.get_json()
    try:
        response = requests.post(f'{BACKEND_URL}/login_fiscal', json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

@app.route('/all_active_spots_per_street', methods=['POST'])
def get_all_vagas_ativas_por_rua():
    data = request.get_json()
    cidade = data.get('cidade')
    rua = data.get('rua')
    if not cidade:
        return jsonify({'message': 'Cidade não fornecida.'}), 400
    if not rua:
        return jsonify({'message': 'Rua não fornecida.'}), 400
    try:
        response = requests.post(f'{BACKEND_URL}/all_active_spots_per_street', json={'cidade': cidade, 'rua': rua})
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

@app.route('/all_expired_spots_per_street', methods=['POST'])
def get_all_vagas_expiradas_por_rua():
    data = request.get_json()
    cidade = data.get('cidade')
    rua = data.get('rua')
    if not cidade:
        return jsonify({'message': 'Cidade não fornecida.'}), 400
    if not rua:
        return jsonify({'message': 'Rua não fornecida.'}), 400
    try:
        response = requests.post(f'{BACKEND_URL}/all_expired_spots_per_street', json={'cidade': cidade, 'rua': rua})
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

# Rota para obter a vaga ativa
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

# Rota para obter todas as vagas do cliente
@app.route('/all_spots', methods=['POST'])
def get_all_spots():
    data = request.get_json()
    placa_do_carro = data.get('placaDoCarro')
    if not placa_do_carro:
        return jsonify({'message': 'Placa do carro não fornecida.'}), 400
    try:
        response = requests.post(f'{BACKEND_URL}/all_spots', json={'placaDoCarro': placa_do_carro})
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

@app.route('/all_cities', methods=['GET'])
def get_all_cidades():
    try:
        response = requests.get(f'{BACKEND_URL}/all_cities')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

@app.route('/all_streets', methods=['POST'])
def get_all_ruas():
    data = request.get_json()
    cidade = data.get('cidade')
    if not cidade:
        return jsonify({'message': 'Cidade não fornecida.'}), 400
    try:
        response = requests.post(f'{BACKEND_URL}/all_streets', json={'cidade': cidade})
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

@app.route('/all_spots_per_street', methods=['POST'])
def get_all_vagas_por_rua():
    data = request.get_json()
    cidade = data.get('cidade')
    rua = data.get('rua')
    if not cidade:
        return jsonify({'message': 'Cidade não fornecida.'}), 400
    if not rua:
        return jsonify({'message': 'Rua não fornecida.'}), 400
    try:
        response = requests.post(f'{BACKEND_URL}/all_spots_per_street', json={'cidade': cidade, 'rua': rua})
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

# Rota para comprar vaga
@app.route('/buy_spot', methods=['POST'])
def buy_spot():
    data = request.get_json()
    print(data)
    placa_do_carro = data.get('placaDoCarro')
    cidade = data.get('cidade')
    rua = data.get('rua')
    tempo = data.get('tempo')

    if not placa_do_carro:
        return jsonify({'message': 'Placa do carro não fornecida.'}), 400
    if not cidade:
        return jsonify({'message': 'Cidade não fornecida.'}), 400
    if not rua:
        return jsonify({'message': 'Rua não fornecida.'}), 400
    if not tempo:
        return jsonify({'message': 'Tempo não fornecido.'}), 400
    
    try:
        # Verifica vaga ativa
        get_active_spot_response = requests.post(f'{BACKEND_URL}/active_spot', json={'placaDoCarro': placa_do_carro})
        if get_active_spot_response.status_code == 200:
            active_spot_data = get_active_spot_response.json()
            if active_spot_data.get('rua') == rua:
                # Adiciona tempo à vaga ativa
                response = requests.post(f'{BACKEND_URL}/add_time_to_spot', json={'placaDoCarro': placa_do_carro, 'tempo': tempo})
            else:
                # Expira vaga ativa e cria nova vaga
                requests.post(f'{BACKEND_URL}/expire_spot', json={'placaDoCarro': placa_do_carro})
                response = requests.post(f'{BACKEND_URL}/buy_spot', json={'placaDoCarro': placa_do_carro, 'cidade': cidade, 'rua': rua, 'tempo': tempo})
        else:
            # Cria nova vaga
            response = requests.post(f'{BACKEND_URL}/buy_spot', json={'placaDoCarro': placa_do_carro, 'cidade': cidade, 'rua': rua, 'tempo': tempo})
        
        return jsonify(response.json()), response.status_code
    
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Erro ao conectar ao backend.', 'error': str(e)}), 500

@app.route('/get_info', methods=['POST'])
def get_info():
    data = request.get_json()
    placa_do_carro = data.get('placadocarro')
    cpf = data.get('cpf')
    if not placa_do_carro:
        return jsonify({'message': 'Placa do carro não fornecida.'}), 400
    try:
        client_info = requests.post(f'{BACKEND_URL}/cliente_info', json={'placadocarro': placa_do_carro}).json()
        fiscal_info = requests.post(f'{BACKEND_URL}/fiscal_info', json={'cpf': cpf}).json()
        return jsonify({"client_info":client_info, "fiscal_info":fiscal_info}), 200
    except Exception as e:
        return jsonify({'message': 'Erro ao obter informações do cliente.', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)

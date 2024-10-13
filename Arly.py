from flask import Flask, request
from pyngrok import ngrok

# Inicializar o Flask
app = Flask(__name__)

# Variável global para armazenar o token
token_armazenado = None

# Rota que será chamada pelo Brightspace após a autenticação
@app.route('/callback')
def callback():
    global token_armazenado
    token = request.args.get('token')  # Captura o token da URL de redirecionamento
    if token:
        token_armazenado = token  # Armazena o token
        return f"Token recebido e armazenado: {token}", 200
    else:
        return "Token não encontrado", 400

# Iniciar ngrok para expor a porta 5000 (onde o Flask estará rodando)
public_url = ngrok.connect(5000)
print(f"URL pública do ngrok: {public_url}")

# Rodar o servidor Flask
app.run(port=5000)

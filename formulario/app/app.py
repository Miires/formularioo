from flask import Flask, request, jsonify, render_template
import re
import jwt
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "chave_secreta_jwt"
API_KEY = "chave-secreta-123"

@app.route("/")
def home():
    return render_template("index.html")

def validar_dados(nome, email, senha):
    if len(nome) < 3:
        return False, "Nome muito curto."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Email inválido."
    if not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", senha):
        return False, "Senha fraca."
    return True, ""

@app.route("/registrar", methods=["POST"])
def registrar():
    if request.headers.get("x-api-key") != API_KEY:
        return jsonify({"message": "Acesso negado."}), 403

    dados = request.get_json()
    valido, erro = validar_dados(dados["nome"], dados["email"], dados["senha"])
    if not valido:
        return jsonify({"message": erro}), 400

    token = jwt.encode({
        "sub": dados["email"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
    }, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({"message": "Usuário registrado!", "token": token})

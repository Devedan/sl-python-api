from flask import Flask, request, jsonify

app = Flask(__name__)

# La même clé que dans le script Luau
TOKEN_VALIDE = "MaCleSecrete123!"

@app.route('/api', methods=['POST'])
def recevoir_donnees():
    # Vérification du Token dans les headers
    token_recu = request.headers.get("X-API-Key")
    
    if token_recu != TOKEN_VALIDE:
        return jsonify({"status": "erreur", "message": "Accès refusé : Token invalide"}), 403

    # Si le token est bon, on traite la donnée
    data = request.get_json()
    return jsonify({"status": "succès", "message": "Authentification réussie !"})


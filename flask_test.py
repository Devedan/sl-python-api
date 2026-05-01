## 2. Côté Serveur : Le script Python (Flask)
## Ce script doit être hébergé sur un serveur web (comme Heroku, PythonAnywhere ou un VPS). [3, 4] 

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api', methods=['POST'])

def recevoir_donnees():
    # Récupération du JSON envoyé par Second Life
    data = request.get_json()
    
    if not data:
        return jsonify({"status": "erreur", "message": "Pas de données"}), 400
    
    nom_objet = data.get("objet_nom")
    valeur = data.get("valeur")
    
    print(f"Reçu de Second Life : L'objet {nom_objet} a envoyé {valeur}")
    
    # Réponse renvoyée à Second Life
    return jsonify({
        "status": "succès",
        "message": f"Serveur Python a bien reçu {valeur}"
    }), 200

if __name__ == '__main__':
    app.run(port=5000)

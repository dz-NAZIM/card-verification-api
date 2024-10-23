import requests
import json

# URL de l'API
url = "http://127.0.0.1:7070/verify_card"  # Utilisez l'URL locale

# Données de la carte de crédit
data = {
    "number": "4242424242424242",
    "exp_month": 12,
    "exp_year": 2024,
    "cvc": "123"
}

# Envoi de la requête POST
response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

# Affichage de la réponse
print(response.status_code)  # Affiche le code de statut HTTP
try:
    print(response.json())       # Affiche la réponse JSON
except ValueError:
    print("Erreur de décodage JSON:", response.text)  # Affiche le contenu brut de la réponse


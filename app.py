from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

stripe.api_key = "sk_test_your_stripe_api_key"

@app.route('/verify_card', methods=['POST'])
def verify_card():
    data = request.json
    try:
        # Créer un token de carte avec Stripe
        token = stripe.Token.create(
            card={
                "number": data['number'],
                "exp_month": data['exp_month'],
                "exp_year": data['exp_year'],
                "cvc": data['cvc'],
            },
        )
        return jsonify({"status": "success", "token": token.id}), 200
    except stripe.error.CardError as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


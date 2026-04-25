from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# config
client = Client("hasnatz/bangla_multilable_news_classifier")



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict(): #prediction
    try:
        user_data = request.json
        news_text = user_data.get("text", "")

        if not news_text:
            return jsonify({"error": "No text provided"}), 400

        result = client.predict(
            text=news_text,
            api_name="/predict" 
        )

        # 3. Return the result from HF back to your Flask user
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
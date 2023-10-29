from flask import Flask, request, jsonify
from flask_cors import CORS
from tweets import process_data  # Import the function from the tweets module
from linkedin import process_data_l
from model import process_data_f

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Welcome to the Flask app!"

@app.route("/contact2", methods=["POST"])
def contact2():
    try:
        data = request.get_json()
        linkedin = data.get("firstName")
        twitter = data.get("lastName")
        
        response_data = {"linkedin": linkedin, "twitter": twitter}
        
        # Call the process_data function from the tweets module
        result = process_data(response_data["twitter"])
        result_l = process_data_l(response_data["linkedin"])
        finale  = process_data_f()
        
        return jsonify({
            "finale":finale
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

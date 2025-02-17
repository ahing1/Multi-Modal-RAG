from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from config import TRITON_URL
from utils import cache_request, store_cache

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    """ Handles inference requests and returns Triton Server response. """
    data = request.json

    # Check Redis Cache
    cached_response = cache_request(data)
    if cached_response:
        return jsonify({"cached": True, "response": cached_response})

    # Send request to Triton
    response = requests.post(TRITON_URL, json=data)

    if response.status_code == 200:
        output = response.json()
        store_cache(data, output)  # Cache the response
        return jsonify({"cached": False, "response": output})
    else:
        return jsonify({"error": "Failed to process request", "status_code": response.status_code}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    if not urls:
        return jsonify({"error": "No URLs provided"}), 400

    result = []

    for url in urls:
        try:
            response = requests.get(url)
            data = response.json()
            numbers = data.get("numbers")
            if numbers and isinstance(numbers, list):
                result.extend(numbers)
        except Exception as e:
            print(f"Error fetching data from {url}: {str(e)}")

    return jsonify({"numbers": result})
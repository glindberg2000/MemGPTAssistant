import requests  # for making HTTP requests to MemGPT API
from flask import Flask, request, jsonify  # Flask imports


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    # Make API call to MemGPT here
    # For demonstration, let's assume the answer is "42"
    answer = "42"
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run()

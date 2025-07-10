# server/app.py

from flask import Flask, jsonify

# Create an instance of the Flask class. This is our web application.
app = Flask(__name__)

# --- API Endpoints (Our "Routes") ---

@app.route("/")
def index():
    """
    This is the main endpoint. It's what you see when you visit
    the base URL of our server.
    """
    # jsonify is a Flask function that converts a Python dictionary
    # into a JSON response, which is the standard for APIs.
    return jsonify({
        "message": "👋 Hello from Project-Bridge! Our server is running.",
        "status": "ok"
    })

# We will add more endpoints here later for our notes!
# For example: @app.route("/notes")

# This block allows us to run the app directly with "python server/app.py"
# The "debug=True" part is very helpful for development, as it will
# automatically reload the server when you save changes.
if __name__ == '__main__':
    app.run(debug=True)
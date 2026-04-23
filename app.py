# My GitHub token (DO NOT COMMIT)
github_token = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the DAST testing app!"

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    html = f"<h1>Hello, {name}!</h1>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

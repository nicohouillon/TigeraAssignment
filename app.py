from flask import Flask, request, jsonify

import fetch

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def api():
    return fetch.main()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
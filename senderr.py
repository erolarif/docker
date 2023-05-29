from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Merhaba, Docker konteynerinden geliyorum!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

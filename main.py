from flask import Flask, jsonify
from sptrans import get_monitoramento

app = Flask(__name__)

@app.route('/')
def home():
    return "🚌 API de Monitoramento SPTrans - Linha 2013-10"

@app.route('/linha/2013-10')
def linha_2013():
    resultado = get_monitoramento()
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

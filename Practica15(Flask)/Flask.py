from flask import Flask

app = Flask(__name__)

ALLOWED_IP = '10.2.81.75'

@app.route('/')
def hola_mundo():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
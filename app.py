from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "✅ La IA creadora está activa desde Render y funcionando 24/7."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

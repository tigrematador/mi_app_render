from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola desde la nube con Render!' 

if __name__ == '__main__':
    app.run()

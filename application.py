from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anime')
def anime():
    return render_template('anime.html')

@app.route('/konoha')
def konoha():
    return render_template('konoha.html')

@app.route('/hokage')
def hokage():
    return render_template('hokage.html')

if __name__ == "__main__":
    app.run(debug=True)

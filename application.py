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

@app.route('/fhokage')
def fhokage():
    return render_template('fhokage.html')

@app.route('/petenarwiki.herokuapp.com/hokage')
def hokage():
    return render_template('hokage.html')

@app.route('/petenarwiki.herokuaoo.com/narbir')
def narbir():
    return render_template('narbir.html')

@app.route('//petenarwiki.herokuapp.com/petenarwiki.herokuapp.com/konoha')
def konoha2():
    return render_template('konoha2.html')

if __name__ == "__main__":
    app.run(debug=True)

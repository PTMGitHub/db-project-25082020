from flask import render_template 
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

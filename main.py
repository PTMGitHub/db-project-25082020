from psycopg2 import connect
from flask import render_template 
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    return render_template("index.html")
    
    # # declare connection instance
    # conn = psycopg2.connect(
    #     dbname = "postgres",
    #     user = "postgres",
    #     host = "0.0.0.0:5001",
    #     password = "root"
    # )

    # # execute an SQL statement using the psycopg2 cursor object
    # cur.execute("SELECT * FROM movies;")
    # for record in cur:
    #     print record

    # # close the cursor object to avoid memory leaks
    # cur.close()

    # # close the connection as well
    # conn.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')

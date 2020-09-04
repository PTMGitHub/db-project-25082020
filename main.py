from psycopg2 import connect
from flask import render_template 
from flask import Flask


t_host = "db" # this will be either "localhost", a domain name, or an IP address.
t_port = "5432" # default postgres port
t_dbname = "postgres"
t_user = "postgres"
t_pw = "root"
db_conn = connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()


app = Flask(__name__)
@app.route('/')
@app.route('/index', methods=['GET'])
def hello():


    #return render_template("index.html")
    query = "SELECT movie_name FROM movies;"
    db_cursor.execute(query)

    movies = db_cursor.fetchall()
    
    

    return render_template("index.html", movies = movies)



if __name__ == "__main__":
    app.run(host='0.0.0.0')

db_conn.close()
from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route('/afvink3')
def Connect_database():
    conn = mysql.connector.connect(host='ensembldb.ensembl.org',user ='anonymous',db='homo_sapiens_core_95_38')

    return 'Hello World!'


if __name__ == '__main__':
    app.run()

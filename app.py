from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/afvink3', methods=["POST"])
def webpagina():
    rows= connect_database()
    return render_template("Afvink3.html", database=rows)


def connect_database():
    conn = mysql.connector.connect(host='ensembldb.ensembl.org',
                                   user='anonymous',
                                   db='homo_sapiens_core_95_38')
    cursor = conn.cursor()
    cursor.execute("select description from gene")
    #rows = cursor.fetchall()
    rows = cursor.fetchall()
    des =[]
    for row in rows:
        if str(row) != "(None,)":
            des.append(row)

    cursor.close()
    conn.close()
    return des


if __name__ == '__main__':
    app.run()

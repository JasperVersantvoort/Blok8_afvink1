# Naam Jasper Versantvorot
# Functie: Een ensembldb database openen,
# hierin de discription tonen die je kan filteren op een zoekwoord


from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/afvink3', methods=["POST", "GET"])
def webpagina():
    """

    :return: De website
    """
    if request.method == "POST":
        zoek = request.form.get("zoek", "")
        rows = connect_database(zoek)

        return render_template("Afvink3.html", database=rows, zoek=zoek)

    else:
        rows = connect_database("None")
        return render_template("Afvink3.html", database=rows, zoek="None")


def connect_database(zoek):
    """ haalt de description uit de ensembldb database
     en filtert deze op het zoekwoord

    :param zoek: Het ingegeven zoekwoord
    :return: Een lijst met de juiste discriptions
    """
    print("zoek woord is: ", zoek)
    conn = mysql.connector.connect(host='ensembldb.ensembl.org',
                                   user='anonymous',
                                   db='homo_sapiens_core_95_38')
    cursor = conn.cursor()
    cursor.execute("select description from gene")
    rows = cursor.fetchall()
    des = []
    for row in rows:
        if str(row) != "(None,)":
            if zoek in str(row) or zoek is None:
                des.append(row)

    cursor.close()
    conn.close()
    return des


if __name__ == '__main__':
    app.run()

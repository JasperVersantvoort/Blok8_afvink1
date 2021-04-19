# Naam Jasper Versantvorot
# Functie: Een ensembldb database openen,
# hierin de discription tonen die je kan filteren op een zoekwoord


from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
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
    print("zoek woord is:", zoek)
    conn = mysql.connector.connect(host='ensembldb.ensembl.org',
                                   user='anonymous',
                                   db='homo_sapiens_core_95_38')
    cursor = conn.cursor()
    cursor.execute("select description from gene")
    rows = cursor.fetchall()
    des = []
    for row in rows:
        if str(row) != "(None,)":
            if zoek.upper() in str(row).upper():
                pos_start = str(row).upper().index(zoek.upper())
                pos_end = pos_start + len(zoek)

                woord = str(row)[pos_start:pos_end]
                split_row = str(row).upper().split(zoek.upper())
                regel = []
                for i in range(len(split_row)):
                    regel.append(split_row[i])
                    if i != len(split_row)-1:
                        regel.append(woord)
                des.append(regel)




            elif zoek == 'None':
                des.append(row)

    cursor.close()
    conn.close()
    return des


if __name__ == '__main__':
    app.run()

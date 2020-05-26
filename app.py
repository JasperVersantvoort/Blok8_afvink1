from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)


@app.route('/afvink3', methods=["POST", "GET"])
def webpagina():
    if request.method =="POST":
        zoek = request.form.get("zoek", "")
        rows = connect_database(zoek)

        return render_template("Afvink3.html", database=rows, zoek=zoek)

    else:
        rows = connect_database("None")
        return render_template("Afvink3.html", database=rows, zoek="None")


def connect_database(zoek):
    print("zoek woord is: ",zoek)
    conn = mysql.connector.connect(host='ensembldb.ensembl.org',
                                   user='anonymous',
                                   db='homo_sapiens_core_95_38')
    cursor = conn.cursor()
    cursor.execute("select description from gene")
    rows = cursor.fetchall()
    des = []
    for row in rows:
        # print (row)
        if str(row) != "(None,)":
            # print(row)
            if zoek in str(row) or zoek is None:
                des.append(row)
                # print (des)

    cursor.close()
    conn.close()
    return des


if __name__ == '__main__':
    app.run()

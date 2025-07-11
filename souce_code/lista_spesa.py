from flask import Flask, request
import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="thomas",
    password="Th0M4s!",
    database="db_spesa")

cnx.autocommit = True

app = Flask(__name__)

@app.route("/aggiungiOggetto/")
def aggiungi_oggetto():
    '''
    - aggiungere oggetto a lista
        - nome utente
        - lista della spesa
        - oggetto
    ''' 
    nome = request.args.get('nome')
    lista = request.args.get('lista')
    oggetto = request.args.get('oggetto')
    try:
        # provo ad aggiungere l'oggetto alla lista 
        # dando per scontato che esista sia nome che lista
        ...
    except:
        # se fallisce lo step di prima o manca solo la lista
        # o manca anche il nome
        try:
            # provo a vedere se manca solo la lista
            # creando una nuova lista
            ...
        except:
            # se fallisce significa che manca anche il nome
            # e allora creo tutto
            ...
    return "Oggetto aggiunto"

@app.route("/togliOggetto/")
def togli_oggetto():
    '''
    - togliere oggetto a lista
        - nome utente
        - lista della spesa
        - oggetto
    '''
    nome = request.args.get('nome')
    lista = request.args.get('lista')
    oggetto = request.args.get('oggetto')
    try:
        ...
    except:
        return "Oggetto non trovato"
    return "Oggetto rimosso"

@app.route("/vediLista/")
def vedi_lista():
    '''
    - vedi lista della spesa
        - nome utente
        - lista della spesa
    '''
    nome = request.args.get('nome')
    lista = request.args.get('lista')
    try:
        ...
    except:
        return "Lista non trovata"

@app.route("/rimuoviLista/")
def rimuovi_lista():
    '''
    - rimuovi lista della spesa
        - nome utente
        - lista della spesa
    '''
    nome_utente = request.args.get('nome')
    nome_lista = request.args.get('lista')
    try:
        cur = cnx.cursor()
        cur.execute("DELETE FROM liste " \
                    " WHERE     nome = %s " \
                    "       AND id_utente IN (SELECT id " \
                    "                           FROM utenti " \
                    "                          WHERE nome = %s);"
                   ,(nome_lista, nome_utente))
        return "Lista rimossa"
    except:
        return "Lista non trovata"

if __name__ == '__main__':
    app.debug = True
    app.run()
    # Close connection
    cnx.close()
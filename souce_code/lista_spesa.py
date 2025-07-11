from flask import Flask, request , jsonify
import mysql.connector

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
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
    cur = cnx.cursor()
    try:
        # provo ad aggiungere l'oggetto alla lista 
        # dando per scontato che esista sia nome che lista
        cur.execute("""
        INSERT INTO oggetti (nome, id_lista)
        SELECT %s, l.id
        FROM liste l
        JOIN utenti u ON l.id_utente = u.id
        WHERE l.nome = %s AND u.nome = %s
    """, (oggetto, lista, nome))

        if cur.rowcount == 0:
            raise Exception("Lista o utente non trovati")
        
    except:
        try:
            # provo a vedere se manca solo la lista
            # creando una nuova lista
            cur.execute("""
                INSERT INTO liste (nome, id_utente)
                SELECT %s, id FROM utenti WHERE nome = %s
            """, (lista, nome))
            # ora aggiungo l’oggetto
            cur.execute("""
                INSERT INTO oggetti (nome, id_lista)
                SELECT %s, l.id
                FROM liste l
                JOIN utenti u ON l.id_utente = u.id
                WHERE l.nome = %s AND u.nome = %s
            """, (oggetto, lista, nome))
                        
            if cur.rowcount == 0:
                raise Exception("Lista o utente non trovati")
        except:
            # se fallisce significa che manca anche il nome
            # e allora creo tutto
            cur.execute("INSERT INTO utenti (nome) VALUES (%s)", (nome,))
            id = cur.lastrowid
            cur.execute("""
                INSERT INTO liste (nome, %i)
                SELECT %s, id FROM utenti WHERE nome = %s
            """, (id ,lista, nome))
            
            cur.execute("""
                INSERT INTO oggetti (nome, id_lista)
                SELECT %s, l.id
                FROM liste l
                JOIN utenti u ON l.id_utente = u.id
                WHERE l.nome = %s AND u.nome = %s
            """, (oggetto, lista, nome))
            
            return "Oggetto non inserito"
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
    cur = cnx.cursor()
    try:
        cur.execute("""
            DELETE FROM oggetti 
            WHERE nome = %s 
              AND id_lista IN (
                  SELECT l.id FROM liste l
                  JOIN utenti u ON l.id_utente = u.id
                  WHERE l.nome = %s AND u.nome = %s
              )
        """, (oggetto, lista, nome))
        if cur.rowcount == 0:
            raise Exception("Oggetto non trovato")
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
    cur = cnx.cursor()
    try:
        cur.execute("""
            SELECT o.nome
            FROM oggetti o
            JOIN liste l ON o.id_lista = l.id
            JOIN utenti u ON l.id_utente = u.id
            WHERE l.nome = %s AND u.nome = %s
        """, (lista, nome))
        risultati = cur.fetchall()
        if not risultati:
            raise Exception("Lista vuota o non trovata")
        return jsonify([row[0] for row in risultati])
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

    cur = cnx.cursor()
    cur.execute("""
        DELETE FROM liste 
        WHERE nome = %s 
          AND id_utente IN (
              SELECT id FROM utenti WHERE nome = %s
          )
    """, (nome_lista, nome_utente))
    if cur.rowcount > 0:
        return "Lista rimossa"
    else:
        return "Lista non trovata"

if __name__ == '__main__':
    app.run(debug = True)
    cnx.close()

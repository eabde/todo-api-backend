from flask import Flask, request

app = Flask(__name__)
liste :dict[str,dict[str,set[str]]] = {}

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
        liste[nome][lista].add(oggetto)
    except:
        # se fallisce lo step di prima o manca solo la lista
        # o manca anche il nome
        try:
            # provo a vedere se manca solo la lista
            # creando una nuova lista
            liste[nome][lista]={oggetto}
        except:
            # se fallisce significa che manca anche il nome
            # e allora creo tutto
            liste[nome]={lista:{oggetto}}
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
        liste[nome][lista].remove(oggetto)
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
        return list(liste[nome][lista])
    except:
        return "Lista non trovata"

@app.route("/rimuoviLista/")
def rimuovi_lista():
    '''
    - rimuovi lista della spesa
        - nome utente
        - lista della spesa
    '''
    nome = request.args.get('nome')
    lista = request.args.get('lista')
    try:
        del liste[nome][lista]
        return "Lista rimossa"
    except:
        return "Lista non trovata"

if __name__ == '__main__':
    app.debug = True
    app.run()
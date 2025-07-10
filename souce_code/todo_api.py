from flask import Flask, request

app = Flask(__name__)
liste :dict[str,set[str]] = {}

@app.route("/aggiungiOggetto/")
def aggiungi_oggetto():
    '''
    - aggiungere oggetto a lista
        - nome utente
        - oggetto
    ''' 
    nome = request.args.get('nome')
    oggetto = request.args.get('oggetto')
    try:
        liste[nome].add(oggetto)
    except:
        liste[nome]={oggetto}
    return "Oggetto aggiunto"

@app.route("/togliOggetto/")
def togli_oggetto():
    '''
    - togliere oggetto a lista
        - nome utente
        - oggetto
    '''
    nome = request.args.get('nome')
    oggetto = request.args.get('oggetto')
    try:
        liste[nome].remove(oggetto)
    except:
        return "Oggetto non trovato"
    return "Oggetto rimosso"

@app.route("/vediLista/")
def vedi_lista():
    '''
    - vedi lista della spesa
        - nome utente
    '''
    nome = request.args.get('nome')
    try:
        return list(liste[nome])
    except:
        return "Lista non trovata"

@app.route("/rimuoviLista/")
def rimuovi_lista():
    '''
    - rimuovi lista della spesa
        - nome utente
    '''
    nome = request.args.get('nome')
    try:
        del liste[nome]
        return "Lista rimossa"
    except:
        return "Lista non trovata"

if __name__ == '__main__':
    app.debug = True
    app.run()
from flask import Flask, request

app = Flask(__name__)
elenco = []

@app.route("/aggiungiVoce/")
def aggiungi_voce():
    voce = request.args.get('voce')
    elenco.append({'descrizione':voce, 'completato': False})
    return "Aggiunto"

@app.route("/visualizzaVoci/")
def visualizza_voci():
    tipo = request.args.get('tipo')
    completato = None
    if tipo == 'completato':
        completato = True
    elif tipo == 'non completato':
        completato = False
    return list(filter(lambda e: e['completato']==completato or completato==None,elenco))

if __name__ == '__main__':
    app.debug = True
    app.run()


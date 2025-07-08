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
    stato = request.args.get('stato')
    completato = None
    if stato == 'completato':
        completato = True
    elif stato == 'non completato':
        completato = False
    return list(filter(lambda e: e['completato']==completato or completato==None,elenco))

@app.route("/cambiaStatoVoce/")
def cambia_stato_voce():
    voce = request.args.get('voce')
    stato = request.args.get('stato')
    for el in elenco:
        if el['descrizione'] == voce:
            el['completato'] = True if stato == 'completato' else False
    return 'Modificato'

if __name__ == '__main__':
    app.debug = True
    app.run()


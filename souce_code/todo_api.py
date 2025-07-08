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
    return elenco

if __name__ == '__main__':
    app.debug = True
    app.run()


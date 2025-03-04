import os
from flask import Flask, render_template, jsonify

# Flask nyní hledá šablony v aktuální složce i v "templates/"
app = Flask(__name__, template_folder=".")

quotes = [
    "Život je to, co se děje, když jste zaneprázdněni jinými plány.",
    "Největší slávou v životě není nikdy nepadnout, ale zvednout se pokaždé, když padneme.",
    "Štěstí není něco hotového. Přichází to z vašich vlastních činů.",
    "Nečekejte. Čas nebude nikdy správný.",
    "Úspěch je jít od neúspěchu k neúspěchu bez ztráty nadšení."
]

@app.route("/")
def home():
    if not os.path.exists("index.html"):
        return "Chyba: Soubor index.html nebyl nalezen!", 500
    return render_template("index.html")

@app.route("/api/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

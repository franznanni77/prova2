from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML minimalista integrato direttamente nel codice (uso di render_template_string)
HTML_PAGE = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Calcolo Somma e Moltiplicazione</title>
    </head>
    <body>
        <h1>Somma e Moltiplicazione di due numeri</h1>
        <form method="POST">
            <label for="numero1">Numero 1:</label>
            <input type="text" id="numero1" name="numero1" value="{{ numero1 }}" />
            <br><br>
            
            <label for="numero2">Numero 2:</label>
            <input type="text" id="numero2" name="numero2" value="{{ numero2 }}" />
            <br><br>
            
            <button type="submit">Calcola</button>
        </form>
        
        {% if somma is not none and moltiplicazione is not none %}
            <hr>
            <p><strong>Somma:</strong> {{ somma }}</p>
            <p><strong>Moltiplicazione:</strong> {{ moltiplicazione }}</p>
        {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    numero1 = ""
    numero2 = ""
    somma = None
    moltiplicazione = None

    if request.method == "POST":
        # Prendiamo i valori dal form (input name="numero1" e name="numero2")
        numero1 = request.form.get("numero1", "")
        numero2 = request.form.get("numero2", "")

        try:
            # Convertiamo i valori in float per calcolare
            num1_float = float(numero1)
            num2_float = float(numero2)
            
            somma = num1_float + num2_float
            moltiplicazione = num1_float * num2_float
        except ValueError:
            # Gestione veloce di eventuali errori di conversione
            pass

    # Renderizziamo la pagina HTML passando le variabili
    return render_template_string(
        HTML_PAGE,
        numero1=numero1,
        numero2=numero2,
        somma=somma,
        moltiplicazione=moltiplicazione
    )

if __name__ == "__main__":
    app.run(debug=True)

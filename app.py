from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def dog_main():
    if request.method == "POST":
        resp = request.form
        a = resp.get('dnm')

        if a == '1':
            result = 'Rs.25000'
            return render_template("husky.html", abc=result)

        if a == '2':
            result = 'Rs.35000'
            return render_template("Labrador.html", abc=result)

        if a == '3':
            result = 'Rs.45000'
            return render_template("golden.html", abc=result)
        if a == '4':
            result = 'Rs.20000'
            return render_template("bulldog.html", abc=result)

    else:
        return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True)

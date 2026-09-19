from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/info", methods=["GET", "POST"])
def get_info():
    submitted_info = None

    if request.method == "POST":
        submitted_info = {
            "name": request.form.get("name", "").strip(),
            "age": request.form.get("age", "").strip(),
        }

    return render_template("info.html", submitted_info=submitted_info)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", box_number = 3)

@app.route("/<int:box_number>")
def box_number(box_number):
    return render_template("index.html", box_number = box_number)

@app.route("/<int:box_number>/<color>")
def color(box_number, color):
    return render_template("index.html", box_number = box_number, color = color)

if __name__=="__main__":
    app.run(debug=True)

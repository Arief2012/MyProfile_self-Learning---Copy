from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/main")
def profile():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)
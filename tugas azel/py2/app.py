from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Fungsi untuk menghitung kecocokan cinta (secara acak)
def calculate_love(name1, name2):
    # Logika sederhana: gabungkan panjang kedua nama, kemudian dapatkan angka acak
    love_score = random.randint(50, 100)  # Angka kecocokan acak antara 50 hingga 100
    return love_score

@app.route("/", methods=["GET", "POST"])
def index():
    love_score = None
    name1 = name2 = ""
    if request.method == "POST":
        name1 = request.form["name1"]
        name2 = request.form["name2"]
        love_score = calculate_love(name1, name2)
    
    return render_template("index.html", love_score=love_score, name1=name1, name2=name2)

if __name__ == "__main__":
    app.run(debug=True)

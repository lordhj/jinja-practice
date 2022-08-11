from flask import Flask, render_template
import random, datetime

app = Flask(__name__)

@app.route('/')
def main():
    random_num = random.randint(1, 10)
    current_year = int(datetime.datetime.now().year)
    return render_template("index.html", num=random_num, year=current_year)

if __name__ == "__main__":
    app.run(debug= True)
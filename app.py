import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_nums():
    nums = []

    for i in range(6):
        lotto_number = random.randint(0,48)
        nums.append(lotto_number)
    return nums

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/generate")
def generate():
    nums = get_nums()
    return jsonify(nums)

if (__name__) == "__main__":
    app.run(debug=True)
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)


# Oregon Megabucks distinct number generator (numbers 1-48)
def get_megabucks_nums():
    nums = random.sample(range(1,49), 6)
    return nums


# Mega Millions number generator (5 distinct regular nums 1-70 and one nondestinct Mega Ball number (1-24))
def get_mega_millions_nums():
    nums = random.sample(range(1, 71), 5)
    mega_ball_number = random.randint(1,24)
    nums.append(mega_ball_number)
    return nums

# Pick 4 number generator (numbers can repeat)
def get_pick4_nums():
    nums = []

    for i in range(4):
        lotto_number = random.randint(0,9)
        nums.append(lotto_number)
    return nums

# Powerball number generator (5 distinct regular nums 1-70 and one nondestinct Mega Ball number (1-24))
def get_powerball_nums():
    nums = random.sample(range(1, 70), 5)
    powerball_number = random.randint(1,26)
    nums.append(powerball_number)
    return nums

# Keno number generator (8 distinct nums from 1-80)
def get_keno_nums():
    nums = random.sample(range(1,81), 8)
    return nums

# app routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate/megabucks")
def generate_megabucks():
    nums = get_megabucks_nums()
    return jsonify(nums)


@app.route("/generate/mega-millions")
def generate_mega_millions():
    nums = get_mega_millions_nums()
    return jsonify(nums)


@app.route("/generate/pick4")
def generate_pick4():
    nums = get_pick4_nums()
    return jsonify(nums)


@app.route("/generate/powerball")
def generate_powerball():
    nums = get_powerball_nums()
    return jsonify(nums)


@app.route("/generate/keno")
def generate_keno():
    nums = get_keno_nums()
    return jsonify(nums)

if (__name__) == "__main__":
    app.run(debug=True)
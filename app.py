import os
from flask import Flask, render_template
import socket
import random

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "pink": "#be2edd",
    "yellow": "#ffff00",
    "white": "#ffffff",
    "purple": "#7d3c98"
}

# Define the color variable (uncomment one or modify as needed)
# color = os.environ.get('APP_COLOR') or random.choice(["red", "green", "white", "pink", "blue", "yellow"])

@app.route("/")
def main():
    color = os.environ.get('APP_COLOR') or random.choice(["red", "green", "white", "pink", "blue", "yellow"])
    print(color
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    with open("/data/testfile.txt") as f:
        contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

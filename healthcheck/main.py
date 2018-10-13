from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def test():
    return str(1/random.randint(0, 3))

if __name__ == "__main__":
    app.run(host="0.0.0.0")

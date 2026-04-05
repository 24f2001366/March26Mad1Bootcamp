from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    x = 10
    return f"hello {x}"

app.run()
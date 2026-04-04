from flask import Flask

xyz = Flask(__name__)

@xyz.route('/')
def home():
    x = 10
    return f"hello {x}"


xyz.run()
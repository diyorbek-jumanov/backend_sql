from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():

    return 'ok'


app.run(debug=True)
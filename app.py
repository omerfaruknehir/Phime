from flask import *

app = Flask(__name__, static_folder="public", template_folder="public")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_file('public/icon.svg')

app.run(host="localhost", port=80, debug=True)
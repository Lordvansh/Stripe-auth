from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask is working on Vercel"

@app.route('/check')
def check():
    return "✅ /check is working too"

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)
    data = response.json()
    entries = data[:5]
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = [quote.text.strip() for quote in soup.select('.text')]
    return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True)

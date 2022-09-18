from flask import Flask, render_template,request
import requests


app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=eaec96d00ac34296bc4dc11964819fe8"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    # articles = news["articles"] 

    # my_articles = []
    # my_news = ""
    return render_template('index.html',cases = case)
@app.route('/sports')
def sports():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=eaec96d00ac34296bc4dc11964819fe8"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('sports.html',cases = case)

@app.route('/business')
def business():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=eaec96d00ac34296bc4dc11964819fe8"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('business.html',cases = case)

@app.route('/technology')
def technology():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=eaec96d00ac34296bc4dc11964819fe8"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('tech.html',cases = case)

@app.route('/science')
def science():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=eaec96d00ac34296bc4dc11964819fe8"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('science.html',cases = case)

@app.route('/health')
def health():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=eaec96d00ac34296bc4dc11964819fe8"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('health.html',cases = case)
if __name__ == '__main__':
    app.run(debug=True)
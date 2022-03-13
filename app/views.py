# from turtle import title
from turtle import title
from flask import render_template
from app import app
from .request import get_random_quotes, get_quote

# Views
@app.route('/')
def index():

    # Getting random quotes

    random_quotes = get_random_quotes()
    print(random_quotes)

   
    title = 'Home - Quotes and more Quotes'
    return render_template('index.html', title = title, random = random_quotes )

@app.route('/quote/<int:id>')
def quote(id):

    quote = get_quote(id)
    author = f'{quote.author}'
   
    return render_template('quote.html', author = author,quote=quote)
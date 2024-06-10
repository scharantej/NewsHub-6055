
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'mysecretkey'
db = SQLAlchemy(app)

class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news_articles')
def news_articles():
    news_articles = NewsArticle.query.all()
    return render_template('news_articles.html', news_articles=news_articles)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # ищет файл в templates/home.html

@app.route('/about')
def about():
    return render_template('about.html')  # ищет файл в templates/about.html

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)





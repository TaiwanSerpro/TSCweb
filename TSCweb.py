from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

# 中文頁面
@app.route('/')
def home():
    return render_template('index.html', lang = 'zh-TW')

@app.route('/about')
def about():
    return render_template('about.html',lang = 'zh-TW')

@app.route('/products')
def products():
    return render_template('products.html',lang = 'zh-TW')

@app.route('/contact')
def contact():
    return render_template('contact.html',lang = 'zh-TW')

# 英文頁面
@app.route('/en')
def home_en():
    return render_template('index_en.html', lang = 'en')

@app.route('/en/about')
def about_en():
    return render_template('about_en.html', lang = 'en')

@app.route('/en/products')
def products_en():
    return render_template('products_en.html', lang = 'en')

@app.route('/en/contact')
def contact_en():
    return render_template('contact_en.html', lang = 'en')
if __name__ == '__main__':
    app.run(debug=True)
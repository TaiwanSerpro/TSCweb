from flask import Flask, render_template, send_from_directory, Response
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

# robots.txt route
@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

# sitemap.xml route
@app.route('/sitemap.xml')
def sitemap():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://tscweb.onrender.com/</loc></url>
    <url><loc>https://tscweb.onrender.com/about</loc></url>
    <url><loc>https://tscweb.onrender.com/products</loc></url>
    <url><loc>https://tscweb.onrender.com/contact</loc></url>
    <url><loc>https://tscweb.onrender.com/en</loc></url>
    <url><loc>https://tscweb.onrender.com/en/about</loc></url>
    <url><loc>https://tscweb.onrender.com/en/products</loc></url>
    <url><loc>https://tscweb.onrender.com/en/contact</loc></url>
</urlset>"""
    return Response(xml_content, mimetype='application/xml')



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
    app.run()
    
    
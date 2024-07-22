from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        'shop_name': 'My Shop'
    }
    return render_template('base.html', **context)

@app.route('/category/<string:category_name>')
def category(category_name):
    products = {
        'clothing': ['Куртка', 'Футболка', 'Джинсы'],
        'shoes': ['Кроссовки', 'Ботинки', 'Сандалии']
    }
    context = {
        'shop_name': 'My Shop',
        'category_name': category_name.capitalize(),
        'products': products.get(category_name, [])
    }
    return render_template('category.html', **context)

@app.route('/product/<string:product_name>')
def product(product_name):
    context = {
        'shop_name': 'My Shop',
        'product_name': product_name
    }
    return render_template('product.html', **context)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
# flask instance
app = Flask(__name__)

# decorator function
@app.route('/') 
# view function
def home():
    return "Hello World , this is home"  #data to be returned

@app.route('/products')
def products():
    return "Products selection"

@app.route('/sales')
def sales():
    return "Sales selection"

@app.route('/stock')
def stock():
    return "Stock selection"




app.run()
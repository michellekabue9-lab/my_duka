from flask import Flask, render_template
# flask instance
app = Flask(__name__)

# decorator function
#index route
@app.route('/') 
# view function
def home():
    return render_template('index.html')  #data to be returned


#products route
@app.route('/products')
def products():
    return render_template('products.html')


#sales route
@app.route('/sales')
def sales():
    return render_template('sales.html')

#stock route
@app.route('/stock')
def stock():
    return render_template('stock.html')

#dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#register route

@app.route('/register')
def register():
    return render_template('register.html')

#login route

@app.route('/login')
def login():
    return render_template('login.html')






app.run()
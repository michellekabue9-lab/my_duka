import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="myduka",
    user="postgres",
    password="michaelkabue@123"
)    
#cur=conn.cursor()
#cur.execute("Select * from products")
#rows=cur.fetchall()
#for row in rows:
 #   print(row)
#cur.close()
#conn.close()

#cur.execute("""
#Select table_name
#from information_schema.tables 
#where table_schema='public'
#""")
#for table in cur.fetchall():
 #   print(table)

curr = conn.cursor()

def get_products():
  curr.execute('Select * from products')
  products_data = curr.fetchall()
  return products_data

def get_stock():
    curr.execute("Select * from stock")
    stock_data = curr.fetchall()
    return stock_data

def get_sales():
    curr.execute("select * from sales")
    sales_data = curr.fetchall()
    return sales_data

# curr.execute("Insert into products(name, buying_price, selling_price) values('fridge',89000,102000)")
# conn.commit()
# print(products_data)

product1 = ('samsung phone', 30000, 40000)
product2 = ('LG Microwave', 50000,60000)


#insert_products(product1)
#insert_products(product2)

def insert_products2(values):
    curr.execute("insert into products(name, buying_price,selling_price)values(%s,%s,%s)", values)
    conn.commit()

product3 = ('books',1200,1300)
insert_products2(product3)

def insert_stock(values):
    curr.execute("insert into stock(pid,stock_quantity) values(%s,%s)",values)
    conn.commit()

def insert_sales(values):
    curr.execute("insert into sales(pid, quantity) values(%s,%s)", values)
    conn.commit()


stock1 = (1,67,)
insert_stock(stock1)
stock2=(2,35)
insert_stock(stock2)

sale1 = (1, 45,)
insert_sales(sale1)
sale2=(2,35)
insert_sales(sale2)

def sales_per_day():
    curr.execute("""
         select date(sales.created_at) as date , sum(sales.quantity * products.buying_price) as total_sales from sales 
        join products on products.id = sales.pid group by date;
    """)
    daily_sales=curr.fetchall()
    return daily_sales

def profit_per_day():
    curr.execute("""
         select date(sales.created_at) as date, sum(sales.quantity * (products.selling_price - products.buying_price))
         as profit from products join sales on sales.pid = products.id group by date;
     """)
    daily_profit=curr.fetchall()
    return daily_profit

def sales_per_products():
    curr.execute("""
         select products.name as p_name , sum(sales.quantity * products.buying_price) 
         as total_sales from sales join products on products.id = sales.pid group by p_name;
     """)
    product_sales=curr.fetchall()
    return product_sales
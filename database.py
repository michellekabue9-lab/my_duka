import psycopg2

#establishing a new connection to a postgres db
conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='michaelkabue@123',dbname='myduka')

#cur object for db opperations
cur=conn.cursor()

cur.execute("select * from products")
products_data=cur.fetchall()
print(products_data)

cur.execute("select * from sales")
sales_data=cur.fetchall()
print(sales_data)

cur.execute("insert into products(name,buying_price,selling_price)values('coat',400,300)")
conn.commit()
print(products_data)

def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

products1=('Sumsung,phone',30000,40000)
products2=('LG,TV',50000,60000)

insert_products(products1)
insert_products(products2)

def insert_products2(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values(%s,%s,%s)",values)
    conn.commit()

product3=('book',1200,1300)
insert_products2(product3)

def get_products():
    cur.execute("select * from products")
    products_data=cur.fetchall()
    return products_data

sales per day select date(sales.created_at)as date,sum(sum.quantity*products.selling_price)as total_sales 
from sales join ptoducts on products.pid=sales.pid group by date;

def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    con.commit()

sales1=(5,33)
sales2=(4,32)

insert_sales(sales1)
insert_sales(sales2)

print(sales_data)

def get_stock():
    cur.execute("select * from stock")
    stock_data=cur.fetchall()
    return stock_data

def insert_stock(values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{values}")
    con,commit()

stock1=(45,78)
stock2=(98,44)

insert_stock(stock1)
insert_stock(stock2)
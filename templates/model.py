from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Product(base):
	__tablename__="products"
	id=Column(Integer,primary_key=True)
	name=Column(String)
	price=Column(String)
	picture_link=Column(String)
	description=Column(String)
	"""docstring for Product"basef 
	__tablename__="products"__ini
	Name=Column(String)
	Price=
	Picture Link=
	Description=t__(self, arg):
		super(Product,base._
		__tablename__="products"_init__()
		self.arg = arg"""
class Cart(base):
	__tablename__="Cart"
	id=Column(Integer,primary_key=True)
	product_id=Column(Integer)
		




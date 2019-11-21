from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name,price,picture_link, description):
	product=Product(name=name,price=price,picture_link=picture_link,description=description)
	session.add(product)
	session.commit()

def edit_id(id,name,price,picture_link, description):
	product=session.query(Product).filter_by(id=id).one()
	product.name=name
	product.price=price
	product.picture_link=picture_link
	product.description=description	
	session.commit()

def delete_by_id(id):
	session.query(Product).filter_by(id=id).one().delete()
    session.commit()

			
def return_all():
	return session.query(Product).all()

def return_by_id(id):
	return session.query(Product).filter_by(id=id).one()	
def add_to_cart(product_id):
	product=Cart(product_id=product_id)
	session.add(product)
	session.commit()

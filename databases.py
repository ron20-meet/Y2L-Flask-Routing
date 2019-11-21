from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name,price,picture link, description):
	product=Product(name=name,price=price,picture=picture_link,description=description)
def edit_id():

def delete_by_id():
	session.query(product).filter_by(
       name=their_name).delete()
   session.commit()

			
def return_all():
	pass
def return_by_id():
	pass

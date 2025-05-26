from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Amazon", founding_year=1994)

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

freebie1 = Freebie(item_name="Mug", value=5, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Notebook", value=8, company=company2, dev=dev1)
freebie3 = Freebie(item_name="Sticker", value=1, company=company1, dev=dev2)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

class Person(base):
    __tablename__ = 'people'
     
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname",String)
    lastname = Column("lastname",String)
    gender = Column("gender",CHAR)
    age = Column("age",Integer)

    def __init__(self, ssn, first, last, gender, age):   
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender 
        self.age = age
    def  __repr__ (self):
        return f"({self.ssn}, {self.firstname}, {self.lastname}, {self.gender}, {self.age})"
class thing (base):
    __tablename__ = 'things'
    tid = Column("tid", Integer, primary_key=True)
    description =Column("description",String)
    owner = Column("owner",Integer, ForeignKey('people.ssn'))

engine = create_engine('sqlite:///people.db', echo=True)
base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
person = Person(24315, "mechael", "lee", "F", 15)
session.add(person)
session.commit()


p1 = Person(123456789, "michael", "jackson", "M", 35)
p2= Person(987654321, "anna", "john", "F", 30)
p3 = Person(987654321, "karter", "voight", "M", 25)
session.add(p1)
session.add(p2)
session.add(p3)
session.commit()
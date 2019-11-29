# import de sqlalchemy
from sqlalchemy import Column, Boolean, String, Integer, Numeric
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Tweet:
	__tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    nom = Column('nom', String(10))
    prenom = Column('message', String(10))
    genre = Column('gender', Boolean)
    pseudo = Column('like', String(10))


    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)
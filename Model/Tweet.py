from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, String, Integer, Numeric

# import de sqlalchemy
Base = declarative_base() 

class Tweet(Base):
    """
    Model de tweet pour le projet flgaz
    """
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    user = Column('user',String(10))
    message = Column('message',String(50))
    img = Column('img', String(50), nullable=True)
    like = Column('like', Integer, nullable=True)


    # methode magique pour print()
    def __str__(self):
        return "{} : \n {}".format(self.user, self.message)


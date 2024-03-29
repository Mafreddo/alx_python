''' this module contains the class State and an instance of class Base '''
    
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
''' importing attributes from SQLAlchemy '''

Base = declarative_base()


class State(Base):
    ''' creating class States that inherits from Base '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
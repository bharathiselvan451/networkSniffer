from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
  
# create an in-memory SQLite database 
engine = create_engine('sqlite:///database.db', echo=True) 
  
Base = declarative_base() 
  
class Devices(Base): 
    __tablename__ = 'Devices'
    MAC_address = Column(String, primary_key=True) 
    IP_address = Column(String) 
    Device_name = Column(String)
    vendour = Column(String)
    File_name = Column(String)
     
  
     
  
# create the Devicess table 
Base.metadata.create_all(engine) 
  
# create a session to manage the connection to the database 
Session = sessionmaker(bind=engine) 
session = Session() 
  
# add a new Devices to the database 
 
  
# query the Devicess table 

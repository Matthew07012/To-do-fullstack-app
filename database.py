#tools needed to connect database
from sqlalchemy import create_engine 

#tools needed to create database sessions 
#sessions used to read, add, delete, etc data
from sqlalchemy.orm import sessionmaker 

#importing base class for database models
#reads from python and translates to databse
from sqlalchemy.orm import declarative_base

#sqlite database url 
#creates a file called todo in project folder
DATABASE_URL = "sqlite:///./todo.db"

#creating engine which is the connection between python and database
engine = create_engine(
    DATABASE_URL,
    
    #allows database to handle multiple threads
    connect_args={"check_same_thread": False} 
)

#creating a session factory used to talk to the database
SessionLocal = sessionmaker(
    #wont commit unless told to
    autocommit = False,
    #wont psuh certain changes until certin queries
    autoflush  = False,
    #bind the session to the engien created 
    bind = engine

)

#base class that database table inherit from
Base = declarative_base()


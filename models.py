#column type from SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

#creating a task model
#then switch to a database model
class Task(Base):

    __tablename__ = "tasks"
    #index = helps jump straight into the search instead of searching the database row one by one
    id = Column(Integer, primary_key = True, index = True)
    task = Column(String)
    completed = Column(Boolean, default = False)
from pydantic import BaseModel

#creating a schema for creating a task
#controls what user is allowed to send when creating a task
class TaskCreate(BaseModel):
    task: str

#schema for returning a task
class TaskResponse(BaseModel):

    id: int
    task: str
    completed: bool

    #allow pydantic to read from sqlalchemy model 
    #because pydantic expects dictionary style data
    class Config:
        from_attributes = True


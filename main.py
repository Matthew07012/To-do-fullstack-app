# Import FastAPI framework
from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
# Import database session tools
from sqlalchemy.orm import Session
# Import database connection + Base
from database import SessionLocal, engine, Base
import models 
import schemas


#main backend app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_db():

    # Create database session
    db = SessionLocal()

    try:
        # Give session to API endpoint
        yield db

    finally:
        # Close session after request finishes
        db.close()



#create GET endpoint for "/"
#GET is to search
@app.get("/")

def home():
    
    return{"message": "My to do APi is running"}

#GET endpoint for task
@app.get("/tasks", response_model= list[schemas.TaskResponse])

def get_tasks(db: Session = Depends(get_db)):    

    tasks = db.query(models.Task).all()
    
    return tasks

#get task by id
@app.get("/tasks/{task_id}", response_model= schemas.TaskResponse)

def get_tasks_id(task_id: int, db: Session = Depends(get_db)):

    task = (
        db.query(models.Task)
        .filter(models.Task.id == task_id)
        .first()
    )
    
    if task is None:
         
         raise HTTPException(status_code=404, detail="Task not found")
    
    return task
    
   


#post used to add new task
#taskresponse to tell what to give back
@app.post("/tasks", response_model = schemas.TaskResponse)

def create_task(task_data: schemas.TaskCreate, db: Session = Depends(get_db)):

    # Create a new Task object using the Task model
    #task data is create by object calss TaskCreate so .task is a variable accessed
    new_task = models.Task(
        task= task_data.task,
        completed=False
    )

    # Add the new task to the database session
    db.add(new_task)

    # Save the change permanently
    db.commit()

    # Refresh to get the generated ID from the database
    db.refresh(new_task)

    # Return the saved task
    return new_task


#deleting task
#has extension because delete asks which tasks to delete
@app.delete("/tasks/{task_id}")

def delete_tasks(task_id: int, db: Session =  Depends(get_db)):

    task = (
        db.query(models.Task)
        .filter(models.Task.id == task_id)
        .first()
        )
    if task is None:
            
            raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)

    db.commit()

    return {"message": "Task deleted"}
#put is to change 
@app.put("/tasks/{task_id}/completed")

def completed_tasks(task_id: int, db: Session = Depends(get_db)):

    task = (
            db.query(models.Task)
            .filter(models.Task.id == task_id)
            .first()
        )
    
    if task is None:
        
            raise HTTPException(status_code=404, detail="Task not found")
    
    task.completed = True

    db.commit()
    
    db.refresh(task)

    return task



//connecting backend to frontend

const API_URL = "https://to-do-fullstack-app.onrender.com/tasks";

window.onload = loadTask;

//async used when connecting frontend to backend as it allows us to wait for response from backend before executing next line of code
//fuction to load tasks from the backend and display them on the frontend
async function loadTask() {
    
     // Send GET request to backend API
     const response = await fetch(API_URL);

    // Convert response from JSON into JavaScript object
    const tasks = await response.json();

    // Get the HTML task list element
    const taskList = document.getElementById("taskList");

    //list used to display not storing so clearing list removes duplicates
    // Clear old list before reloading

    taskList.innerHTML = "";

    // Loop through every task returned from backend
    tasks.forEach(task => {

        // Create new <li> HTML element
        const li = document.createElement("li");

        // Display task information
       const taskText = document.createElement("span");

        taskText.textContent =
         `${task.id}. ${task.task}`;

        if (task.completed) {
     taskText.classList.add("completed");
    }

    li.appendChild(taskText);

        //create complete and delete buttons for each task
        const completeButton = document.createElement("button");
        completeButton.textContent = "Complete";

        completeButton.onclick = function () {
            completeTask(task.id);
    };
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";

        deleteButton.onclick = function (){
            deleteTask(task.id);
        }

        li.appendChild(deleteButton);
        li.appendChild(completeButton);
        // Add task item into HTML list
        taskList.appendChild(li);
    });
}


// Function used to create a new task
async function addTask() {

    // Get input box element
    const input = document.getElementById("taskInput");

    // Get text typed by user
    const taskText = input.value;


    // Send POST request to backend
    await fetch(API_URL, {

        // HTTP method
        method: "POST",

        // Headers describe request format
        headers: {

            // Tell backend we are sending JSON
            "Content-Type": "application/json"
        },

        // Convert JavaScript object into JSON string
        body: JSON.stringify({

            // Task field expected by backend schema
            task: taskText
        })
    });

    input.value = "";
    loadTask();
}
async function completeTask(taskId) {
    
    await fetch(`${API_URL}/${taskId}/completed`, {
        method: "PUT"
    });

    loadTask();
}

async function deleteTask(taskId) {

    await fetch(`${API_URL}/${taskId}`, {
        method: "DELETE"
    });

    loadTask();
}

import { useState, useEffect } from "react";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";


// taskform contains a simple form to set a new task
// tasklist contains a list of tasks that uses functions passed as props to toggle and delete tasks
// tasks will be stored in local storage too by using useEffect hook
// also tasks will be loaded from local storage when the app starts

interface Task {
  id: number;
  text: string;
  completed: boolean;
}

function App() {
  // load local storage tasks, sicronously because local storage is sync
  // const [tasks, setTasks] = useState<Task[]>(() => {
  //   const storedTasks = localStorage.getItem('tasks')
  //   if (storedTasks) {
  //     try {
  //       return JSON.parse(storedTasks)
  //     } catch (error) {
  //       console.error('Error on tasks load')
  //       return []
  //     }
  //   } else {
  //     return []
  //   }
  // });

  // loading tasks via async. emulating an external api call
  const [tasks, setTasks] = useState<Task[]>([])

  const loadTasks = new Promise<Task[]>((resolve, reject) => {
    setTimeout(() => {
      const storedTasks = localStorage.getItem('tasks')
      if (storedTasks) {
        try {
          resolve(JSON.parse(storedTasks))
        } catch (error) {
          console.error('Error on tasks load')
          resolve([])
        }
      } else {
        resolve([])
      }
    }, 2000)
  })

  useEffect(() => {
    const loadTasksAsync = async () => {
      try {
        const tasks = await loadTasks;
        setTasks(tasks);
      } catch (error) {
        console.error('Failed to load tasks:', error);
        setTasks([]); // Opcional: Establece un array vacío en caso de error
      }
    };
    loadTasksAsync();
  }, []);


  useEffect(() => {
    const storedTasks = localStorage.getItem('tasks')
    if (storedTasks) {
      setTasks(JSON.parse(storedTasks))
    }
  }, [])

  useEffect(() => { // stores tasks in local storage
    localStorage.setItem('tasks', JSON.stringify(tasks))
  }, [tasks])

  const addTask = (task: string) => {
    setTasks([...tasks, { id: Date.now(), text: task, completed: false }])
  }
  const toggleTask = (id: number) => {
    setTasks(tasks.map((t: Task) => t.id !== id ? { ...t, completed: !t.completed } : t))
  };

  const deleteTask = (id: number) => {
    setTasks(tasks.filter((t: Task) => t.id !== id))
  }

  return (
    <div>
      <h1>tareas</h1>
      <TaskForm addTask={addTask} />
      <TaskList tasks={tasks} toggleTask={toggleTask} deleteTask={deleteTask} />
    </div>
  );
}

export default App;

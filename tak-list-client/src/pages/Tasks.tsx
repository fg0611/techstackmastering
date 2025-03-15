import { useState, useEffect } from "react";
import TaskForm from "../components/TaskForm";
import TaskList from "../components/TaskList";
import { apiGetTasks, apiAddTask, apiDeleteTask, apiUpdateTask } from "../api/tasks";
import iTask from "../components/interface";

// taskform contains a simple form to set a new task
// tasklist contains a list of tasks that uses functions passed as props to toggle and delete tasks
// tasks will be stored in local storage too by using useEffect hook
// also tasks will be loaded from local storage when the app starts

function Tasks() {
    // load local storage tasks, sicronously because local storage is sync
    const [tasks, setTasks] = useState<iTask[]>([]);

    const loadTasks = async () => {
        const tasks = await apiGetTasks();
        if (tasks) {
            setTasks(tasks)
        }
    }
    
    useEffect(() => {
        loadTasks()
    }, [])

    useEffect(() => { // store tasks in local storage when tasks change
        localStorage.setItem('tasks', JSON.stringify(tasks))
    }, [tasks])

    const addTask = async (task: string) => {
        const newTask = await apiAddTask(task);
        if (newTask) {
            setTasks([...tasks, newTask])
        }
    }
    const completeTask = async (task: iTask) => {
        const updatedTask = await apiUpdateTask({ ...task, completed: !task.completed });
        if (task?.id > 0) {
            const updatedTasks = tasks.map((t: iTask) => t.id === updatedTask.id ? updatedTask : t)
            setTasks(updatedTasks)
        }
    };

    const deleteTask = async (id: number) => {
        const deletedTaskId = await apiDeleteTask(id);
        if (deletedTaskId) {
            console.log('deleted task', deletedTaskId)
            const filteredTasks = tasks.filter((t: iTask) => t.id !== id)
            setTasks(filteredTasks)
        }
    }

    return (
        <div>
            <h1>tareas</h1>
            <TaskForm addTask={addTask} />
            <TaskList tasks={tasks} completeTask={completeTask} deleteTask={deleteTask} />
        </div>
    );
}

export default Tasks;

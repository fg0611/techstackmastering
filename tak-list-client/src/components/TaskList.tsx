import { useState } from "react";
import iTask from "./interface";
import Task from "./Task";

interface TaskListProps {
    tasks: iTask[];
    completeTask: (task: iTask) => void;
    deleteTask: (id: number) => void;
}

enum Filter {
    All = 'all',
    Completed = 'completed',
    Uncompleted = 'uncompleted'
}

function TaskList({ tasks, completeTask, deleteTask }: TaskListProps) {
    const [filter, setFilter] = useState(Filter.All);

    const filteredTasks = tasks.filter((t: iTask) => {
        if (filter === Filter.Completed) return t.completed
        if (filter === Filter.Uncompleted) return !t.completed
        return true
    })

    return (
        <div>
            <select value={filter} onChange={(e) => setFilter(e.target.value as Filter)}>
                <option>{Filter.All}</option>
                <option>{Filter.Completed}</option>
                <option>{Filter.Uncompleted}</option>
            </select>
            <ul key='task-list' id='task-list'>
                {filteredTasks?.length > 0 ?
                    filteredTasks.map(task =>
                        <Task task={task} completeTask={completeTask} deleteTask={deleteTask} />
                    )
                    : <li key={'no items'}>No hay tareas</li>}
            </ul>
        </div>
    )
}

export default TaskList;
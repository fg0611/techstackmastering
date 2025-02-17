
interface Task {
    id: number;
    text: string;
    completed: boolean;
}

interface TaskListProps {
    tasks: Task[];
    toggleTask: (id: number) => void;
    deleteTask: (id: number) => void;
}

function TaskList({ tasks, toggleTask, deleteTask }: TaskListProps) {
    return (
        <ul>
            {tasks?.length > 0 ?
                tasks.map(task =>
                    <li id={task.id.toString()} key={task.id}
                        style={{ gap:"1px", textDecoration: task.completed ? 'line-trhough' : 'none' }}
                    >
                        <span onClick={() => toggleTask(task.id)}>{task.text}</span>
                        <button onClick={() => deleteTask(task.id)}>X</button>
                    </li>
                )
                : <li>No hay tareas</li>}
        </ul>
    )
}

export default TaskList;
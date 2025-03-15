import iTask from "./interface";

interface TaskProps {
    task: iTask;
    completeTask: (task: iTask) => void;
    deleteTask: (id: number) => void;
}

function Task({ task, completeTask, deleteTask }: TaskProps) {
    return (
        <li id={task.id.toString()} key={task.id.toString()}
            style={{ color: task.completed ? 'green' : 'black' }}>
            <button onClick={() => completeTask(task)}>{task.text}</button>
            <button onClick={() => deleteTask(task.id)}>X</button>
        </li>
    )
}

export default Task;
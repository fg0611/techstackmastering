import React, { useState } from "react";

interface TaskFormProps {
    addTask: (task: string) => void;
}

function TaskForm({ addTask }: TaskFormProps) {

    const [newTask, setNewTask] = useState('');

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => { setNewTask(e.target.value) }

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (!newTask.trim()) return
        addTask(newTask);
        setNewTask('');
    }

    return (
        <form onSubmit={handleSubmit}>
            <input
                type='text'
                placeholder='Escribe una tarea'
                value={newTask}
                onChange={handleChange}
            />
            <button type='submit'>Agregar</button>
        </form>
    )
}

export default TaskForm;
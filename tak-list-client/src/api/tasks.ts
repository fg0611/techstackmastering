import axios from 'axios'
import iTask from '../components/interface';

const API_URL = 'https://jsonplaceholder.typicode.com/todos'; // Usamos una API falsa

export const apiGetTasks = async () => {
    try {
        const response = await axios.get(`{API_URL}`);
        if (response.status > 199 && response.status < 300) {
            console.log('response', response.data);
            return response.data;
        }
        return null;
    } catch (error) {
        console.error('Error on get task', error);
        return null;
    }
};
export const apiGetTask = async (id: number) => {
    try {
        const response = await axios.get(`{API_URL}/${id}`);
        return response.data;
    } catch (error) {
        console.error('Error on get task', error);
        return null;
    }
};

export const apiAddTask = async (text: string) => {
    try {
        const res = await axios.post(API_URL, { id: Date.now(), text: text, completed: false });
        if (res.status > 199 && res.status < 300)
            return res.data;
    } catch (error) {
        console.error('Error on add task', error);
        return null;
    }
}

export const apiDeleteTask = async (id: number) => {
    try {
        const res = await axios.delete(`{API_URL}/${id}`);
        if (res.status > 199 && res.status < 300)
            return id;
        return null;
    }
    catch (error) {
        console.error('Error on delete task', error);
        return null;
    }
}

export const apiUpdateTask = async (task: iTask) => {
    const { data } = await axios.put(`${API_URL}/${task.id}`, task);
    return data;
}

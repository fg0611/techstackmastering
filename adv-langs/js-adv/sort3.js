function findWord(arr) {
    // Paso 1: Construir un grafo de precedencias
    const graph = new Map();
    const inDegree = new Map();

    // Inicializar el grafo y el grado de entrada
    for (const relation of arr) {
        const [from, to] = relation.split('>');
        if (!graph.has(from)) graph.set(from, []);
        if (!graph.has(to)) graph.set(to, []);
        if (!inDegree.has(from)) inDegree.set(from, 0);
        if (!inDegree.has(to)) inDegree.set(to, 0);

        graph.get(from).push(to); // Añadir arista de "from" a "to"
        inDegree.set(to, inDegree.get(to) + 1); // Incrementar el grado de entrada de "to"
    }

    // Paso 2: Encontrar el nodo inicial (grado de entrada = 0)
    const queue = [];
    for (const [node, degree] of inDegree.entries()) {
        if (degree === 0) {
            queue.push(node);
        }
    }

    // Paso 3: Orden topológico (BFS)
    const result = [];
    while (queue.length > 0) {
        const node = queue.shift();
        result.push(node);

        // Reducir el grado de entrada de los nodos adyacentes
        for (const neighbor of graph.get(node)) {
            inDegree.set(neighbor, inDegree.get(neighbor) - 1);
            if (inDegree.get(neighbor) === 0) {
                queue.push(neighbor);
            }
        }
    }

    // Paso 4: Devolver la palabra resultante
    return result.join('');
}

// Prueba
console.log(findWord(["I>N", "A>I", "P>A", "S>P"])); // Debería imprimir "SPAIN"
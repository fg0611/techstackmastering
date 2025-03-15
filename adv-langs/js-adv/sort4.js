function findWord(rules) {
    let graph = {};
    let inDegree = {};
    
    // Inicializar el grafo y los grados de entrada
    for (let rule of rules) {
        let [from, to] = rule.split('>');
        if (!graph[from]) graph[from] = new Set();
        if (!graph[to]) graph[to] = new Set();
        graph[from].add(to);
        
        // Inicializar inDegree para cada nodo
        if (!(from in inDegree)) inDegree[from] = 0;
        if (!(to in inDegree)) inDegree[to] = 0;
        inDegree[to]++; // Incrementar grado de entrada del nodo dependiente
    }
    
    // Cola para nodos con in-degree 0 (sin dependencias)
    let queue = Object.keys(inDegree).filter(char => inDegree[char] === 0);
    let result = [];
    
    while (queue.length) {
        let char = queue.shift();
        result.push(char);
        
        for (let neighbor of graph[char]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] === 0) queue.push(neighbor);
        }
    }
    
    return result.join('');
}

// Pruebas con los ejemplos dados
console.log(findWord(["P>E", "E>R", "R>U"])); // PERU
console.log(findWord(["I>N", "A>I", "P>A", "S>P"])); // SPAIN
console.log(findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"])); // HUNGARY
console.log(findWord(["I>F", "W>I", "S>W", "F>T"])); // SWIFT
console.log(findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"])); // PORTUGAL
console.log(findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"])); // SWITZERLAND

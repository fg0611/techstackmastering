function findWord(arr) {
    // Crear un mapa para almacenar las relaciones de precedencia
    const precedenceMap = new Map();
    const allLetters = new Set();

    // Llenar el mapa con las relaciones de precedencia
    for (const relation of arr) {
        const [prev, next] = relation.split('>');
        precedenceMap.set(prev, next);
        allLetters.add(prev);
        allLetters.add(next);
    }

    // Encontrar la letra inicial (la que no aparece como "next" en ninguna relación)
    let startLetter = '';
    for (const letter of allLetters) {
        if (!Array.from(precedenceMap.values()).includes(letter)) {
            startLetter = letter;
            break;
        }
    }

    // Construir la palabra basada en las relaciones de precedencia
    let word = startLetter;
    let currentLetter = startLetter;
    while (precedenceMap.has(currentLetter)) {
        currentLetter = precedenceMap.get(currentLetter);
        word += currentLetter;
    }

    return word;
}

console.log(findWord(["I>N", "A>I", "P>A", "S>P"])); // Debería imprimir "SPAIN"
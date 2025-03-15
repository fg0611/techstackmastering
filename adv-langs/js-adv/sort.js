// Task Description
// A precedence rule is given as "P>E", which means that letter "P" is followed directly by the letter "E". Write a function, given an array of precedence rules, that finds the word represented by the given rules.
// Note: Each represented word contains a set of unique characters, i.e. the word does not contain duplicate letters.
// Examples:
function findWord(arr) {
    let repeat = true
    let count = 0
    while (repeat && count < 30) {
        count++
        console.log(count)
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i][0] === arr[i + 1][2] || arr[i][2] !== arr[i + 1][0])
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]; // swap         
        }
        let isOrdered = true
        for (let j = 0; j < arr.length - 1; j++) { // aca verificamos si falta ejecutar de nuevo
            if (arr[j][2] !== arr[j + 1][0]) {
                isOrdered = false;
                break
            }
        }
        if (isOrdered) {
            repeat = false
        }
    }
    result = arr.join('').replaceAll('>', '')
    result = new Set(result)
    result = [...result].join('')
    console.log(result)
    return result
}

findWord(["P>E", "E>R", "R>U"]) // PERU

findWord(["I>N", "A>I", "P>A", "S>P"]) // SPAIN
// "I>N", "S>P"

findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]) // HUNGARY
findWord(["I>F", "W>I", "S>W", "F>T"]) // SWIFT
findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]) // PORTUGAL
findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]) // SWITZERLAND

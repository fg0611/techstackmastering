const findword = (arr) => {
    let subs = arr.map(el => el.split('>'))
    let res = []
    let count = 20
    
    while (subs.length & count){
        if (!res.length){
            res.push(subs[0])
            subs.shift()
        }
        for (pair of subs) {
            count--;
            if (res[0][0] === pair[1]) {
                res.unshift(pair)
                subs = subs.filter(el => el !== pair)
            }
            else if (res.slice(-1)[0][1] === pair[0]){
                res.push(pair)
                subs = subs.filter(el => el !== pair)
            }          
        }
    }
    const p1 = (res.slice(0, -1).map(el => el[0])).join('')
    const p2 = res.slice(-1)[0].join('')
    return p1 + p2
}

r = findword(["I>N", "A>I", "P>A", "S>P"]) 
// # sp pa ai in
console.log(r)

r2 = findword(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"])
console.log(r2)
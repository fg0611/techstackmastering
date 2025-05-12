// CLASSES IN JS

class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    saludar() {
        console.log(`Hola me llamo ${this.nombre}`)
    }
}

class Humano extends Persona {
    constructor(nombre, edad, pais) {
        super(nombre, edad);
        this.pais = pais
    }
    presentar() {
        super.saludar();
        console.log(`naci en ${this.pais}`)
    }
}

ramon = new Humano('ramon', 40, 'Venequia')

ramon.presentar()
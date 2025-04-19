class Personaje:
    def __init__(self, nombre, ataque, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida

    def tipo_pj (self):
        return 'personaje'

    def vive(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def atacar(self, enemigo):
        enemigo.vida = enemigo.vida - self.ataque
        print(f"{self.nombre} ha atacado a {enemigo.nombre}")
        # print(f"{self.nombre} {self.vive()}")
        if enemigo.vive():
            print(enemigo.nombre, "aun vive")
        else:
            enemigo.morir()

    def atacar_especial(self, enemigo):
        enemigo.vida = enemigo.vida - self.ataque * 1.3
        self.vida = self.vida * 0.9
        print(f"{self.nombre} ha atacado a {enemigo.nombre} con atq especial")
        print(f"Y {self.nombre} {self.vida}")
        if enemigo.vive():
            print(enemigo.nombre, "aun vive")
        else:
            enemigo.morir()

    def atributos(self):
        print(f"{self.nombre} tiene {self.vida} de vida y {self.ataque} de ataque")


class Guerrero(Personaje):
    def __init__(self, nombre, ataque, vida, arma):
        super().__init__(nombre, ataque, vida)
        # personaje.__init__(self, nombre, ataque, vida)
        self.arma = arma
    
    def tipo_pj (self):
        return 'guerrero'

    def seleccionar_arma(self):
        opcion = int(
            input("Elige el arma del guerrero: (1) Espada (2) hacha (3) Lanza")
        )
        if opcion == 1:
            self.arma = self.arma + 20
        elif opcion == 2:
            self.arma = self.arma + 30 # 100
        elif opcion == 3:
            self.arma = self.arma + 10
        else:
            print("El arma no cambió")

    def atributos(self):
        print(
            f"{self.nombre} tiene {self.vida} de vida, {self.ataque} de ataque y daño adicional de {self.arma}"
        )

    def atacar(self, enemigo):
        enemigo.vida = enemigo.vida - (self.ataque + self.arma)
        print(f"{self.nombre} ha atacado a {enemigo.nombre}")
        if enemigo.vive():
            print(enemigo.nombre, "aun vive")
        else:
            enemigo.morir()

    def atacar_especial(self, enemigo):
        ataque_total = (self.ataque + self.arma) * 1.3
        enemigo.vida = enemigo.vida - ataque_total
        self.vida = self.vida * 0.9
        print(f"{self.nombre} ha atacado a {enemigo.nombre} con atq especial")
        print(f"ataque total = {ataque_total}")
        print(f"Y {self.nombre} {self.vida}")
        if enemigo.vive():
            print(enemigo.nombre, "aun vive")
        else:
            enemigo.morir()

personaje_basico = Personaje("Villano", 5, 200)

# enemigo.atributos()

fran = Guerrero("Fran", 5, 200, 5)

# fran.atributos()

# fran.atacar(enemigo)
# # fran.atacar_especial(enemigo)
# fran.seleccionar_arma()

# fran.atacar(enemigo)

# enemigo.atributos()
# personaje_basico.atributos()
# fran.atributos()

# def intercambio(p1, p2):
#     print('..... intercambio .....')
#     p1.atacar(p2)

# intercambio(personaje_basico, fran)

# fran.atributos()

# fran.seleccionar_arma()

# intercambio(fran, personaje_basico)

# personaje_basico.atributos()


def que_personaje (pj):
    print(f'{pj.nombre} es del tipo {pj.tipo_pj()}')

que_personaje(personaje_basico)
que_personaje(fran)


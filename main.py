class Cuadrado:
    def self(self,lado):
        self.lado = lado
        
    def areacalc(self):
        return self.lado ** 2
    
lado = float(input("Ingrese el valor del lado: "))
exple = Cuadrado(lado)
r = exple.area()
print(f"El area es: {r}")
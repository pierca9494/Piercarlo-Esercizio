class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def muovi (self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distanza_da_origine (self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
punto = Punto(3, 4)
print("Distanza dall'origine:", punto.distanza_da_origine())
punto.muovi(1, -2)
print("Nuove coordinate:", (punto.x, punto.y))
print("Distanza dall'origine:", punto.distanza_da_origine())
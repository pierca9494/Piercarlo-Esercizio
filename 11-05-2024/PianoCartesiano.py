import math

class Piano_cartesiano:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    
        
    def aggiungi_piano(self):
        
        punto = Punto()
        punto.inizia_punto()
        Piano_cartesiano.stampa_piano(punto)
        
    #stampa piano cartesiano 
    def stampa_piano(self):
        print(f"Piano Cartesiano: ({self.x}, {self.y},{self.z})")
        
        


class Punto:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def inizia_punto(self, x, y,z):
        lista_punti = []
        
        for i in lista_punti:
            punto = Punto(x, y,z)
            punto.inizia_punto(i, i,i)
            lista_punti.append(punto)
            Piano_cartesiano.stampa_piano(punto)
        

    def muovi(self, dx, dy):
        
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        """Calculates the distance of the point from the origin (0, 0)."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

# Example usage
p = Punto(3, 4,10)
print("Initial distance from origin:", p.distanza_da_origine())
p.muovi(1, 2)
print("New coordinates:", (p.x, p.y))
print("New distance from origin:", p.distanza_da_origine())

Piano_cartesiano.stampa_piano(p)




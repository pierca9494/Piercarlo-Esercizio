aree = []

def dati_aree(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        aree.append(result)
        return result
    return wrapper

@dati_aree
def area_triangolo(base, altezza):
    return 0.5 * base * altezza

@dati_aree 
def area_quadrato(lato):
    return lato ** 2

@dati_aree
def area_rettangolo(base, altezza):
    return base * altezza

def input_dati():
    print("Calcolo dell'area di triangolo, quadrato e rettangolo")
    
    base_triangolo = float(input("Inserisci la base del triangolo: "))
    altezza_triangolo = float(input("Inserisci l'altezza del triangolo: "))
    area_triangolo(base_triangolo, altezza_triangolo)
    
    lato_quadrato = float(input("Inserisci il lato del quadrato: "))
    area_quadrato(lato_quadrato)
    
    base_rettangolo = float(input("Inserisci la base del rettangolo: "))
    altezza_rettangolo = float(input("Inserisci l'altezza del rettangolo: "))
    area_rettangolo(base_rettangolo, altezza_rettangolo)
    
    print(f"Le aree calcolate sono: {aree}")

input_dati()
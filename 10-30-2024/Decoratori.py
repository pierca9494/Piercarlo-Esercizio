def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Inizio esecuzione della funzione:", funzione.__name__)
        risultato = funzione(*args, **kwargs)
        print("Fine esecuzione della funzione:", funzione.__name__)
        return risultato
    return wrapper


@decoratore_con_argomenti
def somma(a, b):
    return a + b

print(somma(3,4))
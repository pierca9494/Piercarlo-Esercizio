def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        

# Input dall'utente
year = int(input("Inserisci un anno: "))

# Verifica e stampa del risultato
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

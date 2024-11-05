# Function to get vowels and their indices
def trova_vocali(parola):
    vocali = "aeiouAEIOU"
    result = [(index, letter) for index, letter in enumerate(parola) if letter in vocali]
    return result


user_input = input("Inserisci una parola: ")


indici_vocali = trova_vocali(user_input)

print(indici_vocali)


print("Vocali e i loro indici:")
for index, vocali in indici_vocali:
    print(f"Index: {index}, Vocali: {vocali}")

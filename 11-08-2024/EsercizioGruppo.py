

# Domande e risposte per ciascun livello
questions = [
    {"question": "Quanto fa 2 + 2?", "answer": 4},
    {"question": "Quanto fa 5 x 3?", "answer": 15},
    {"question": "La capitale della Francia?", "answer": "Parigi"},
    {"question": "Quanto fa 9 x 9?", "answer": 81},
    {"question": "Nome del cantante Bowie?", "answer": "Bowie"},
    {"question": "Quanto fa 50 / 5?", "answer": 10},
    {"question": "Quanto fa 7 x 8?", "answer": 56},
    {"question": "Quanto fa 144 / 12?", "answer": 12},
    {"question": "Quanto fa 19 + 21?", "answer": 40},
    {"question": "Quanto fa 100 - 37?", "answer": 63}
]

# Funzione per porre una domanda e controllare la risposta
def ask_question(level):
    question = questions[level - 1]["question"]
    correct_answer = questions[level - 1]["answer"]
    answer = input(question + " ")
    return answer == str(correct_answer)

# Funzione per giocare a un livello specifico
def play_level(level, user):
    print(f"Livello {level} ")
    if ask_question(level):
        users_db[user]["score"] += 1
        print("Risposta corretta! Hai guadagnato 1 punto.")
    else:
        print("Risposta errata.")
    print(f"Punteggio attuale: {users_db[user]['score']}")

# Funzione per mostrare i livelli disponibili
def show_available_levels(score):
    max_level = min(score + 1, 10)
    available_levels = list(range(1, max_level + 1))
    print("Livelli disponibili:", available_levels)
    return available_levels

# Funzione principale del gioco


import json, requests, random

def random_number():
    num = random.randint(1,1025)

    url = f"https://pokeapi.co/api/v2/pokemon/{num}"

    response = requests.get(url)
    data = response.json()
    return  (str(id),{
                "name": data["name"],
                "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
                "base_experience": data["base_experience"],
                "weight": data["weight"],
                "height": data["height"]
    })

print(data)
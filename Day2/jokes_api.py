import requests

joke_url = "https://official-joke-api.appspot.com/random_joke"
dad_joke_url = "https://icanhazdadjoke.com/"

def get_random_joke(url_type,mood):
    headers = {"Accept": "application/json"}
    joke = requests.get(url=url_type,headers=headers)
    
    if mood == "dad":
        final_joke = joke.json()["joke"]
    else:
        final_joke = joke.json()["setup"] + " " + joke.json()["punchline"]

    print(final_joke)


mood = input("which type of joke do you want? (random/dad): ")
if mood == "random":
    url_type = joke_url
elif mood == "dad":
    url_type = dad_joke_url
else:
    print("Invalid input. Please choose 'random' or 'dad'.")
    url_type = dad_joke_url


get_random_joke(url_type,mood)
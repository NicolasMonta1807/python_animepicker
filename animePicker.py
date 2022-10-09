from random import choice
from urllib import request

import requests

import json


def internalPicker():
    animes = [
        ["Naruto", "action", "long"],
        ["Shingeki no kyojin", "bizarre", "long"],
        ["Spy X Family", "spies", "short"],
        ["FullMetal Alchemist", "action", "long"]
    ]

    print("What kind of anime do you wanna watch?: ")
    mood = input()

    foundAnime = False

    attempts = 0

    while not foundAnime and attempts <= 10:
        item = choice(animes)
        if item[1] == mood:
            print("You really gotta watch ", item[0])
            foundAnime = True
        attempts += 1

    if not foundAnime:
        print("Couldn't find anything for you")


def apiRecommendations(moodID):

    apiUrl = "https://api.jikan.moe/v4/anime"

    queryParams = {
        'limit': 10,
        'status': "complete",
        'sfw': True,
        'start_date': "2022",
        'genres': moodID
    }

    response = requests.get(
        apiUrl,
        params=queryParams)

    data = response.json()

    if response.status_code == 200:

        with open('response.txt', 'w') as fileManager:
            fileManager.write(json.dumps(response.json(), indent=4))

        animeList = response.json()

    print("*************************")
    print("I guess you should watch: ")
    print()

    for i in range(len(data['data'])):
        print(i + 1, data['data'][i]['title'])


def moodDefiner(mood):

    mood = mood.lower()

    match mood:
        case "action":
            return 1
        case "adventure":
            return 2
        case "comedy":
            return 4
        case "drama":
            return 8
        case "fantasy":
            return 10
        case "romance":
            return 22
        case "sci-fi":
            return 24
        case "slice of life":
            return 36
        case _:
            return 0


def main():

    print("***********************")
    print("WELCOME TO ANIME PICKER")
    print("***********************")

    print()

    while True:
        print("What mood are you in? (Genre): ")
        mood = input()

        moodID = moodDefiner(mood)

        if moodID == 0:
            print("Hmmm... I don't know that yet")
        else:
            break

    apiRecommendations(moodID)


if __name__ == "__main__":
    main()

from random import choice, choices, sample
from urllib import request
import requests
import json


def randomPicker(data):

    animeList = []

    while len(animeList) != 5:
        randomAnime = choice((data['data']))
        if (not (randomAnime in animeList)):
            animeList.append(randomAnime)

    return animeList


def getAPI(moodID):

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

    if response.status_code == 200:
        data = response.json()
        with open('response.json', 'w') as fileManager:
            fileManager.write(json.dumps(response.json(), indent=4))
        return data

    return response.status_code


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

    animeList = randomPicker(getAPI(moodID))

    print("You should watch: ")
    for anime in animeList:
        print("\t-", anime['title'])


if __name__ == "__main__":
    main()

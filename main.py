import requests


def get_meal_data(url_to_ask):
    """get meal name from user and returns requests.models.Response object"""
    while True:
        meal_name = input("Enter meal name: ")
        url_to_ask_name = url_to_ask + meal_name
        response_from_url = requests.get(url_to_ask_name)

        return response_from_url


def main():
    """asking user for meal name, and print received data from url"""
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s='

    meal_data = get_meal_data(url)
    meal_data = meal_data.json()

    if meal_data["meals"] is None:
        print("there is no meals matched")
    else:
        for index, meal in enumerate(meal_data["meals"], 1):
            print(f"{index}- {meal['strMeal']}:\n{meal['strInstructions']}")
            print("-" * 20)


if __name__ == '__main__':
    main()

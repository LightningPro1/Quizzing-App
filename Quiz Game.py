import requests
import random
import sys
counter = 0
questions = ["What is the capitol of ", "How many currencies are used in ", "How many countries border ", "Which continents does this country belong to: ", "How many timezones are there in this country: "]
countries = ["India", "USA", "Brazil", "China", "Argentina", "Singapore", "Russia", "Ukraine", "Portugal", "Nepal", "Pakistan", "Spain", "Germany"]
def random_num(l):
    b = random.randint(0, l - 1)
    return b
while True:
    rand_q = random_num(len(questions))
    rand_c = random_num(len(countries))
    a = input(questions[rand_q] + countries[rand_c] + " in lowercase (or q to quit)")
    if a == "q":
        print("Thank you for playing!")
        print("You got", counter, "questions correct!")
        sys.exit()
    response = requests.get("https://restcountries.com/v3.1/name/" + countries[rand_c])
    response = response.json()
    if rand_q == 0:
        answer = response[0]["capital"][0].lower()
    if rand_q == 1:
        answer = str(len(response[0]["currencies"]))
    if rand_q == 2:
        answer = str(len(response[0]["borders"]))
    if rand_q == 3:
        answer = response[0]["continents"][0].lower()
    if rand_q == 4:
        answer = str(len(response[0]["timezones"]))
    if answer == a.lower():
        print("Your answer is correct!")
        counter += 1
    else:
        print("Your answer is incorrect.")
        print("The correct answer is:", answer)
    print("Your current score is:", counter)
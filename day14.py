from python.project_adv.art import logo, vs
from python.project_adv.game_data import data
# from replit import clear
import random


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, is a {description}, from a {country}"


def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == 'b'


def game():
    print(logo)
    should_continue = True
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()

    while should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower = account_a["follower_count"]
        b_follower = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower, b_follower)

        # clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"Your right, your current score: {score}")
        else:
            should_continue = False
            print(f"Sorry, wrong answer. Your score: {score}")


game()
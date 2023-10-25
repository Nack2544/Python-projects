# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."
# }


# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over."


# # Create an empty dictionary
# empty_dictionary = {}

# # Wipe an existing dictionary
# programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# # print(programming_dictionary)

# # Loop thriugh a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# capital = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
# #  Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited  ": ["Paris", "Lille", "Dijon"], "time_visits": 12},
#     "Germany": [{"cities_visited": ["Berlin", "Dijon", "Lille"]}, {"total_visits": 5}, ""]
# }

# # Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Dijon", "Lille"],
        "total_visited": 12
    },
    {
        "country": "German",
        "cities_visited": ["Paris", "Dijon", "Lille"],
        "total_visited": 25}
]
# print(travel_log["France"])
# print(travel_log["Germany"])
print(travel_log[1]["total_visited"])


# HINT: You can call clear() to clear the output in the console.


# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''
# print(logo)
# print("Welcome to the secret auction program!")

# next_bidder = True
# bid = {}


# def finding_highest_bidder(bidding_record):
#     winner = ""
#     highest_bid = 0
#     for bid in bidding_record:
#         bid_amount = bidding_record[bid]

#         if bid_amount > highest_bid:
#             bid_amount = bidding_record[bid]
#             winner = bid
#     print(f"the winner is {winner} with the total of {bid_amount}")

#     # print(f"The winner is {winner} in the total of {highest_bid}")


# while next_bidder:
#     name = input("What is your name? ")
#     price = int(input("What's your bid?: $"))
#     bid[name] = price

#     should_continue = input(
#         "Are there any other bidders? Type 'yes or 'no':  ").lower()
#     if should_continue == "no":
#         next_bidder = False
#         finding_highest_bidder(bid)
#     elif should_continue == "yes":
#         continue
#     else:
#         print("Try again!")

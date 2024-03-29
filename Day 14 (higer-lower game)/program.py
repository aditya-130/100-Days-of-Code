import assets, game_data, random, os
clear = lambda: os.system("cls")
clear()
print(assets.logo)
user_accounts = game_data.data
game_over = False
score = 0
account_a = random.choice(user_accounts)
if(score == 0):
    user_accounts.remove(account_a)
while not game_over:
    account_b = random.choice(user_accounts)
    print(f"\nCompare A: {account_a['name']}, a {account_a['description']} from {account_a['country']}\n")
    print(assets.vs)
    print(f"\nCompare B: {account_b['name']}, a {account_b['description']} from {account_b['country']}\n")
    user_choice = input("Who has more followers? Type 'A' or 'B: ").upper()
    if user_choice == "A":
        if int(account_a['follower_count']) > int(account_b['follower_count']):
            print("You got it right\n")
            score += 1
            clear()
            print(f"\nYour Score: {score}")
        else:
            game_over = True
            print("You got it wrong")
            print(f"Your Score: {score}")
    elif user_choice == "B":
        if int(account_a['follower_count']) < int(account_b['follower_count']):
            print("You got it right")
            score += 1
            clear()
            account_a = account_b
            user_accounts.remove(account_b)
            print(f"\nYour Score: {score}")
        else:
            game_over = True
            print("You got it wrong")
            print(f"Your Score: {score}")
    else:
        print("Wrong input")
import time
import random
from colorama import Fore
import os

os.system('title Dice Game V1 @ Rotenda Sino')

SL = "-----------------------------------------------"

player_score = 0
boss_score = 0
total_score = f"Your Score : {player_score} | Boss´s Score : {boss_score}"

dice_art = {
    1: (
        "        ┌─────────┐",
        "        │         │",
        "        │    ●    │",
        "        │         │",
        "        └─────────┘",
    ),
    2: (
        "        ┌─────────┐",
        "        │  ●      │",
        "        │         │",
        "        │      ●  │",
        "        └─────────┘",
    ),
    3: (
        "        ┌─────────┐",
        "        │  ●      │",
        "        │    ●    │",
        "        │      ●  │",
        "        └─────────┘",
    ),
    4: (
        "        ┌─────────┐",
        "        │  ●   ●  │",
        "        │         │",
        "        │  ●   ●  │",
        "        └─────────┘",
    ),
    5: (
        "        ┌─────────┐",
        "        │  ●   ●  │",
        "        │    ●    │",
        "        │  ●   ●  │",
        "        └─────────┘",
    ),
    6: (
        "        ┌─────────┐",
        "        │  ●   ●  │",
        "        │  ●   ●  │",
        "        │  ●   ●  │",
        "        └─────────┘",
    ),
}


def print_dice_art(dice, color):
    for line in dice_art[dice]:
        print(color + line, end="")
    print(Fore.RESET)


def print_dice_pair(player_dice, boss_dice):
    print("        You Rolled:       The Boss Rolled:")
    for player_line, boss_line in zip(dice_art[player_dice], dice_art[boss_dice]):
        print(Fore.GREEN + player_line, end=" ")
        print(Fore.RED + boss_line)
    print(Fore.RESET + SL)


print("""
████████▄   ▄█   ▄████████    ▄████████    ▄█  
███   ▀███ ███  ███    ███   ███    ███   ███  
███    ███ ███▌ ███    █▀    ███    █▀    ███
███    ███ ███▌ ███         ▄███▄▄▄       ███ 
███    ███ ███▌ ███        ▀▀███▀▀▀       ██▌ 
███    ███ ███  ███    █▄    ███    █▄    █▀ 
███   ▄███ ███  ███    ███   ███    ███   
████████▀  █▀   ████████▀    ██████████   ▄█                                                                                                                             
""" + Fore.RESET)
time.sleep(0.25)


def play_manual_game():
    global player_score, boss_score, total_score

    while True:

        print("                  Roll The Dice?")
        want_play = input("                  'Y' or 'N' : ").upper()
        print(SL)
        if want_play == "Y":
            time.sleep(0.3)
        elif want_play == "N":
            print(Fore.RED + "                  Run Away Then!")
            print(Fore.RESET + SL)
            exit()
        else:
            print(Fore.RED + "                  Invalid Input!")
            print(Fore.RESET + SL)
            continue

        player_dice = random.randint(1, 6)
        boss_dice = random.randint(1, 6)

        print_dice_pair(player_dice, boss_dice)

        if player_dice < boss_dice:
            boss_score += 1
            print(Fore.RED + "                    You Lost!" + Fore.RESET)
        elif player_dice > boss_dice:
            player_score += 1
            print(Fore.GREEN + "                    You Won!" + Fore.RESET)
        else:
            print("                  It's a Tie!")

        total_score = f"       Your Score : {player_score} | Boss´s Score : {boss_score}"
        print(total_score)
        print(SL)


# ---------------------------------------------


def play_automated_game():
    global player_score, boss_score, total_score

    while True:

        time.sleep(0.5)
        player_dice = random.randint(1, 6)
        boss_dice = random.randint(1, 6)

        print_dice_pair(player_dice, boss_dice)

        if player_dice < boss_dice:
            boss_score += 1
            print(Fore.RED + "                    You Lost!" + Fore.RESET)
        elif player_dice > boss_dice:
            player_score += 1
            print(Fore.GREEN + "                    You Won!" + Fore.RESET)
        else:
            print("                  It's a Tie!")

        total_score = f"       Your Score : {player_score} | Boss's Score : {boss_score}"
        print(total_score)
        print(SL)
        time.sleep(0.4)

# -----------------------------------------------------


while True:

    time.sleep(0.25)
    print(SL)
    time.sleep(0.25)
    print("           What Do You Want To Play ? ")
    time.sleep(0.25)
    print("              'M' -> Manual Game")
    time.sleep(0.25)
    print("             'A' -> Automated Game")
    time.sleep(0.25)
    print(SL)
    time.sleep(0.25)

    while True:

        game_selection = input("               Select Your Game : ").upper()
        time.sleep(0.15)
        print(SL)
        time.sleep(0.15)
        if game_selection == 'M':
            play_manual_game()
        elif game_selection == 'A':
            play_automated_game()
        else:
            print(Fore.RED + "               Invalid Selection")
            time.sleep(0.15)
            print(Fore.RESET + SL)

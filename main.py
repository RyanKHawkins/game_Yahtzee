# Title:  Yahtzee
# Author:  Ryan Hawkins
# Update:  2019-10-28

import random

held_dice = []


def roll_dice(num=5):
    dice = []
    for die in range(num):
        roll = random.randint(1, 6)
        dice.append(roll)
    return dice


def display_dice(dice):
    print("-" * 10)
    print("[{}][{}][{}][{}][{}]".format(*dice))


def evaluate_dice(dice):
    three_of_a_kind = False
    two_of_a_kind = False
    four_of_a_kind = False
    full_house = False
    yahtzee = False
    for die in dice:
        if dice.count(die) == 2:
            two_of_a_kind = True
        if dice.count(die) == 3:
            three_of_a_kind = True
        if dice.count(die) == 4:
            four_of_a_kind = True
        if dice.count(die) == 5:
            yahtzee = True
    if two_of_a_kind == True and three_of_a_kind == True:
        full_house = True

    if full_house is True:
        print("Full House!")
    elif three_of_a_kind is True:
        print("Three of a kind!")
    elif four_of_a_kind is True:
        print("Four of a kind!")
    elif yahtzee is True:
        print("YAHTZEE!!")


def game_play():
    selection = ""
    while selection not in ["1", "2", "3", "4", "5", "0"]:
        selection = input("Which dice would you like to keep? 0 for none")
    selection = int(selection) - 1

    for die in dice:
        if selection == "0":
            break
        else:
            held_dice.append(dice[selection])

    print(held_dice)


for i in range(50):

    dice = roll_dice()
    display_dice(dice)
    evaluate_dice(dice)

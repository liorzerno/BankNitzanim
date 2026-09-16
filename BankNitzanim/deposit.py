# import math
# import pygame
# import random
# import time
# import matplotlib
import datetime
import consts


def create_deposit(checking_account: int, deposit_type: int, interest_type: int, interest_rate: float,
                   deposit_time=int, start_date= datetime):
    """
    :param checking_account: the checking account from which the money will come
    :param deposit_type: 0 or 1 as set in consts - a singular deposit or a monthly deposit
	:param interest_type: 0 or 1 as set in consts - a fixed interest rate or a prime-linked
				          interest rate
	:param interest_rate: the amount of interest that is added to the deposit once a year
	:param deposit_time: the amount of time the money will be deposited
	:param start_date: the day in the game
	:return: a dictionary with the values it received
    """
    initial_deposit = int(input("put in deposit amount"))
    while checking_account < initial_deposit:
        print("you don't have enough to start the deposit")
        initial_deposit = int(input("put in deposit amount"))
    deposit = {"deposit_type": deposit_type, "interest_type": interest_type, "interest_rate": interest_rate,
               "initial_deposit": initial_deposit, "start_date": start_date, "deposit_time": deposit_time,
               "amount_in_deposit": consts.STARTING_DEPOSIT_AMOUNT}

    return deposit


def calc_day_difference(deposit: dict, day_in_game=datetime):
    """
    :param deposit: the deposit
    :param day_in_game: the day in the game
    :return: the number of days that passed since it was opened
    """
    start = deposit["start_date"]
    # difference = day_in_game - start
    difference = (day_in_game - start).Days
    return difference


def can_add_to_deposit(deposit: dict, checking_account: float):
    """
    :param deposit: the deposit we want to put more money in
    :param checking_account: the checking account from which the money will come
    :return: if we can add more money to the deposit
    :return: prints a fitting message
    """
    if deposit["deposit_type"] == 1 and checking_account >= deposit["initial_deposit"]:
        print(f"Transferring {deposit["initial_deposit"]} to deposit from checking account")
        return True
    else:
        print("Transfer failed - one time deposit or not enough in checking account")
        return False


def add_to_deposit(deposit: dict):
    """
    :param deposit: the deposit we want to put more money in
    :return: adds money to the deposit, return an amount to subtract from the checking account
    """
    deposit["amount_in_deposit"] += deposit["initial_deposit"]
    return deposit["initial_deposit"]


def can_draw_deposit(deposit: dict, day_in_game=datetime):
    """
    :param deposit: the deposit we want to draw into the checking account
    :param day_in_game: the day in the game
    :return: if enough time has passed so we can draw the deposit
    :return: prints a fitting message
    """
    if calc_day_difference(deposit, day_in_game) >= deposit["deposit_time"]:
        print(f"Drawing {deposit["deposit_amount"]} from deposit into checking account")
        return True
    else:
        print("deposit draw date has not arrived")
        return False


def can_add_interest(deposit: dict, day_in_game=datetime):
    """
    :param deposit: the deposit we want to add interest to
    :param day_in_game: the day in the game
    :return:
    """
    if (calc_day_difference(deposit, day_in_game)) % consts.YEAR == 0:
        return True
    else:
        return False


def calc_interest(deposit: dict, day_in_game=datetime):
    """
    :param deposit: the deposit to calc interest from
    :param day_in_game: the day in the game
    :return: the interest that was earned while saving
    """
    if can_draw_deposit(deposit, day_in_game):
        interest_earned = deposit["amount_in_deposit"] * deposit["interest_rate"] / 100
    else:
        interest_earned = 0
    return interest_earned


def draw_deposit(deposit: dict):
    """
    :param deposit: the deposit to be drawn into the checking account
    :return: deletes all stats from the deposit
    :return: an amount to add to the checking account
    """
    money_earned = deposit["amount_in_deposit"] + calc_interest(deposit)
    deposit.clear()
    return money_earned

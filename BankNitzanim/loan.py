from datetime import date
import consts

def create_loan(loan_type, interest_type,
                interest_rate, start_date, loan_amount, monthly_amount):
    """
    :param loan_type: 0 or 1 as set in consts - a short term loan or a long term loan
    :param interest_type: 0 or 1 as set in consts - a fixed interest rate or a prime-linked
				interest rate
    :param interest_rate: the amount of interest that is added to the deposit once a year
    :param start_date: the starting date of the deposit
    :param loan_amount: the amount of loan
    :param monthly_amount: the monthly payment
    :return: a dictionary with the values it received
    """
    loan = {"loan_type": loan_type, "interest_type": interest_type, "interest_rate": interest_rate, "start_date": start_date,
            "loan_amount": loan_amount, "monthly_amount": monthly_amount}
    return loan


def pay_monthly(loan: dict):
    """
    :param loan: the loan we want to pay
    :return: the money to remove from checking account
    """
    return loan["monthly_amount"]

def pay_entire_loan(loan: dict):
    """
    :param loan: the loan we want to pay
    :return: the money to remove from checking account
    """
    return loan["loan_amount"]

def calc_interest(loan: dict):
    """
    :param loan: the loan to calc interest from
    :return: the interest that was earned while saving
    """
    interest_earned = loan["loan_amount"] * loan["interest_rate"] / 100
    return interest_earned

def calc_day_difference(loan: dict, day_in_game: date):
    start = loan["start_date"]
    difference = day_in_game - start
    difference = difference.days
    return difference

def can_add_interest(loan: dict, day_in_game: date):
    """
    :param loan: the loan we want to check
    :param day_in_game: the date today (in the game)
    :return: a boolean value that describes whether the loan can add the interest to
    """
    if (calc_day_difference(loan, day_in_game)) % consts.YEAR == 0:
        return True
    else:
        return False

def add_interest(loan: dict):
    loan["loan_amount"] += calc_interest(loan)
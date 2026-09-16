WIDTH, HEIGHT = 800, 600

INITIAL_CHECKING_ACCOUNT = 0
INITIAL_WAGE = 5000
INITIAL_NATIONAL_BANK_INTEREST = 5
INITIAL_PRIME = INITIAL_NATIONAL_BANK_INTEREST + 1.5
SINGULAR_DEPOSIT = 0
MONTHLY_DEPOSIT = 1
DEPOSIT_TYPES = [SINGULAR_DEPOSIT, MONTHLY_DEPOSIT]
FIXED_INTEREST = 0
PRIME_LINKED_INTEREST = 1
INTEREST_TYPES = [FIXED_INTEREST, PRIME_LINKED_INTEREST]

RUNNING_STATE = True

WHITE = (255, 255, 255)

DARK_BLUE = (25,25,112)
DARK_PURPLE = (52, 21 ,57)
BUTTON_X = 300
BUTTON_Y = 300
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 150


DEPOSIT_TEXT = "A deposit is money added to a bank account, for safekeeping or to earn interest.\n It can also refer to a partial payment to secure goods or services, \n such as a security deposit on a rental property."
LOAN_TEXT = "An amount of money that is borrowed from a bank and has to be paid back, \n usually together with an extra amount of money that you have to pay as a charge for borrowing"
INVEST_TEXT = "Investing is the act of putting your money into something with the hope that it will grow over time.\n Think of it like planting a tree. \n You plant a seed (your money), take care of it, and over time, it grows into a big tree (more money)."
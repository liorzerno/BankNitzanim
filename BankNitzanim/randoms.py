import random

bad = {
    "Car Crash" : -500 ,
    "Child Support" : -150 ,
    #""

}

good = {
    "Work Bonus" : 200 ,
    "Money On The Street" : 50 ,
    "Birthday Gift" : 400 ,
    #""
}

def get_random_situation(event):
    if event == 0:
        return random.choice(list(good.items()))

    return random.choice(list(bad.items()))


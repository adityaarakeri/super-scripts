import datetime
from datetime import datetime as dt
currenttime = dt.now().strftime('%I:%M %p')
print(f"The current time is {currenttime}.")


def enterminutes():
    while True:
        minutes = input("How many minutes from now?\n")
        try:
            minutes = int(minutes)
            return minutes
        except ValueError:
            print(f"{minutes} is not a valid number.")


def telltime():
    minutes = enterminutes()
    minutes_added = datetime.timedelta(minutes=minutes)
    futuretime = dt.now() + minutes_added
    print(f"\n{futuretime.strftime('%I:%M %p')}\n")


def exitor():
    exitor_ans = input("Enter '1' if you'd like to input another time. Enter anything else if you'd like to exit.\n")
    if exitor_ans == '1':
        return True
    else:
        return False


while True:
    telltime()
    exitor_ans = exitor()
    if not exitor_ans:
        break

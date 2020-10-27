def celtofah():
    while True:
        cel = input("Input the number of degrees (celsius) that you would like to convert to fahrenheit\n")
        try:
            cel = int(cel)
            break
        except ValueError:
            print(f"{cel} is not a valid input")
    fah = (cel*9/5)+32
    print(f"{cel} degrees celsius is {fah} degrees fahrenheit")


def fahtocel():
    while True:
        fah = input("Input the number of degrees (fahrenheit) that you would like to convert to celsius\n")
        try:
            fah = int(fah)
            break
        except ValueError:
            print(f"{fah} is not a valid input")
    cel = (fah-32)*5/9
    print(f"{fah} degrees celsius is {cel} degrees fahrenheit")


def cel_or_fah():
    while True:
        celfah = input("(1) Convert celsius to fahrenheit OR (2) Convert fahrenheit to celsius\n")
        if celfah == '1':
            celtofah()
            break
        elif celfah == '2':
            fahtocel()
            break
        else:
            print(f"\"{celfah}\" is not a valid input. Enter '1' or '2'")


def exitor():
    exitor_ans = input("Enter '1' if you'd like to input another time. Enter anything else if you'd like to exit\n")
    if exitor_ans == '1':
        return True
    else:
        return False


while True:
    cel_or_fah()
    exitor_ans = exitor()
    if not exitor_ans:
        break

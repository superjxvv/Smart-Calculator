def calculate_tax(income):
    if 0 <= income <= 15527:
        return 0
    if 15528 <= income <= 42707:
        return 15
    if 42708 <= income <= 132406:
        return 25
    if income >= 132407:
        return 28
    return -1


money = int(input())
percent = calculate_tax(money)

print(f"The tax for {money} is {percent}%. That is {round(money * percent / 100)} dollars!")

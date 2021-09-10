def can_buy_alcohol(age):
    can_buy_alcohol = False
    if int(age) >= 18:
        can_bt_alcohol = True
    
    return can_bt_alcohol


print(can_buy_alcohol(18))

def what_can_buy(age):
    if int(age) >= 18:
        print("Can buy alcohol")
    elif int(age) < 18 and int(age) > 14:
        print("Can buy soda")
    else:
        print("Can buy juice")


age = input("what is your age?\n")
what_can_buy(age)
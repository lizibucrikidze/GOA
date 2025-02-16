def manual_lsdigit(user_str):
    digits = "0123456789"
    valid = True


    for char in user_str:
        if char in digits:
            print("correct character")
    else:
        valid = False
        print("Incorrect character")



        print(valid)
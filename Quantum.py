def is_this_a_shirt(x):
    if x != "no":
        x = "no"
        return is_this_a_shirt(x)
    else:
        print("nope.")


you_decide = is_this_a_shirt(input("yes/no"))




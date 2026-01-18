guess_name = "lalal"
guess=" "
guess_count=0
guess_limit=3
while guess_name!=guess and guess_count<=guess_limit:
    if guess_count<guess_limit:
        guess = input("enter a number ")
        print("you have more chances ")
        guess_count += 1
    else:
        guess_count = 4
if guess_count>guess_limit:
    print("you have no chances left")
else:
    print("you guessed it correct")
        
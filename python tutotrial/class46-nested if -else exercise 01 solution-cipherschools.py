winning_number = 18
gu_num = int(input("guess a number between 1 and 100:"))
if winning_number==gu_num:
    print("You win")
else:
    if gu_num<winning_number:
        print("Too low")
    else:
         print("too high")
#import random module 
import random 
random_number = random.randint(100,999)
print(random_number)
inputnumber = int(input("enter your 3 digit guess number"))

while inputnumber!=0:
    num = random_number
    right = 0
    #till when we can get reminder >0 567
    while num%10:
        lastnumber = num%10
        guessedlast = inputnumber%10
        num = num // 10
        inputnumber = inputnumber // 10
        if lastnumber == guessedlast:
            right = right + 1 
    if right == 3:
        print("you did it buddy")
        break 
    else:
        print("%d digits are right" %right)
        inputnumber = int(input("enter your 3 digit guess number"))
else:
    print("you quit the game")

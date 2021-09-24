
# trying basic python stuff

from numpy import negative, positive


Text_Base_Game = 0

if Text_Base_Game == 10: # Motivation Seller

    positive_words = ["yes", "yep"]
    negative_words = ["no", "nah", "NO", "No"]

    print()
    print("Are you feeling Motivated to do some work?")
    intake1 = input(">>> ")

    if intake1 == "no":
 
        print()
        print("Would you like to be motivated?")
        intake2 = input(">>> ")
        
        if intake2 == "yes":

            print()
            print("Then Immediately DO some action")
            print("Like drink water, exercise, read dook, clean something etc.")

        else:
            print()
            print("Then this is not for you, LOSER")
    else:
        print()
        print("Great! Keep Goning")

# Text_Base_Game ends here ....................................................

Text_Calculator = 10
import operator

if Text_Calculator == 10:

    print()
    first_no = int(input("First Number: "))  
    optration1 = input("Mathematical operation: ")
    second_no = int(input("Second Number: "))
    
    optra = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv, "**": operator.pow}
    
    answer = optra[optration1](first_no, second_no)

    print("=>", first_no, optration1, second_no, "=", answer)

# Text_Calculator ends here..................................................
 
















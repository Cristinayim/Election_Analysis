# Initial variable to track game play
user_play = "y"

# While we are still playing...
main_number = 0
while user_play == "y":

    # Ask the user how many numbers to loop through
    counter = int(input("How long should he chain of numbers be?"))
    
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    number = main_number

    #while number < numbers:
    for not_used in range(counter):

        # Print each number in the range
        print(number)
        main_number +=1

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")
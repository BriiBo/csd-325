# Name: Brian Palm
# Assignment: Module 1.3
#
# This program asks the user how many bottles of beer
# are on the wall. The number is passed to a function
# that counts backward to 1.
#
# The program checks that the user enters a positive
# whole number between 1 and 100. At the end, the user
# can choose whether to sing the song again.
# --------------------------------------------------


# Set the maximum number of bottles allowed
MAX_BOTTLES = 100


# This function performs the bottle countdown
def countdown(bottles):

    # Continue looping while more than 1 bottle remains
    while bottles > 1:

        # Display the current number of bottles
        print(f"{bottles} bottles of beer on the wall.")
        print(f"{bottles} bottles of beer.")
        print("Take one down and pass it around.")

        # Subtract one from the number of bottles
        bottles = bottles - 1

        # Use the singular word "bottle" when 1 remains
        if bottles == 1:
            print("1 bottle of beer on the wall.\n")

        # Use the plural word "bottles" for all other numbers
        else:
            print(f"{bottles} bottles of beer on the wall.\n")

    # Display the final verse using the singular word "bottle"
    print("1 bottle of beer on the wall.")
    print("1 bottle of beer.")
    print("Take it down and pass it around.")
    print("No more bottles of beer on the wall.\n")


# Main program starts here

# Set the first response to yes so the program runs at least once
sing_again = "yes"

# Repeat the program if the user enters Y or Yes
while sing_again in {"y", "yes"}:

    # Keep asking until the user enters a valid bottle number
    while True:

        try:
            # Ask the user for the starting number of bottles
            bottle_count = int(
                input(
                    f"Enter the number of bottles of beer "
                    f"on the wall (1-{MAX_BOTTLES}): "
                )
            )

            # Check for zero or a negative number
            if bottle_count <= 0:
                print("Please enter a positive whole number.\n")

            # Check if the number is above the maximum
            elif bottle_count > MAX_BOTTLES:
                print(
                    f"Please enter a number between "
                    f"1 and {MAX_BOTTLES}.\n"
                )

            # The number is valid, so exit the input loop
            else:
                break

        # Handle letters, words, symbols, and decimal numbers
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    # Pass the valid number to the countdown function
    countdown(bottle_count)

    # Remind the user to buy more bottles of beer
    print("Time to buy more bottles of beer!\n")

    # Keep asking until the user enters Yes or No
    while True:

        # Ask whether the user wants to start the program again
        sing_again = input(
            "Would you like to sing the song again? (Y/N): "
        ).strip().lower()

        # Accept Y, Yes, N, or No in any capitalization
        if sing_again in {"y", "yes", "n", "no"}:
            break

        # Display an error for any other response
        print("Please enter Y, Yes, N, or No.\n")

    # Add a blank line before restarting the program
    print()


# This message displays when the user enters N or No
print("Goodbye!")
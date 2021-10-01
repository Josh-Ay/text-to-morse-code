from brain import Brain

print("===============================TEXT TO MORSE CODE CONVERTER=======================================")

brain = Brain()

print("\nWould you like to: \n1. Convert from english to morse code\n2. Convert from morse code to english")
user_choice = input("Choice: ")


try:
    user_choice = int(user_choice)
except ValueError:
    print("\nPlease enter a number. For example: Either '1' or '2'.")
else:
    if user_choice == 1:
        user_input = input("\nPlease enter the string you would like to convert to morse code: ")
        has_sound = input("Would you like sound too? (y/n) ")
        brain.set_sound_option(has_sound)
        translated_message = brain.convert_to_morse(user_input)
        print(f"\nMorse equivalent: {translated_message}")

    elif user_choice == 2:
        user_input = input("\nPlease enter the string you would like to convert to english: ")
        translated_message = brain.convert_to_english(user_input)
        print(f"\nEnglish equivalent: {translated_message}")

    else:
        print("You entered an invalid option. Please try again.")

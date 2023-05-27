from number_to_word.number_to_word import convert_number_to_word

def greet_user():
    '''The "greet_user" function is responsible for the primary user interaction, handling the input, 
    and calling the necessary conversion function to convert the number into its word representation.'''

    print("Hello! Welcome to Number to Word Converter!\nEnter a number and I'll convert it into a word!")
    while True:
        number = input("Enter a number (or 'q' to quit): ")
        if number.lower() == 'q':
            break
        try:
            number = int(number)
            word = convert_number_to_word(number)
            print(f"{word}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("Goodbye!")

if __name__ == "__main__":
    greet_user()
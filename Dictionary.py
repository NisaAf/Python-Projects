import json
from difflib import get_close_matches

# Load the JSON data file containing word definitions
data = json.load(open("data.json"))

def get_definition(word):
    word = word.lower()  # Convert the word to lowercase for case insensitivity
    if word in data:
        return data[word]  # Return the definition if the word is found
    elif len(get_close_matches(word, data.keys())) > 0:
        # Provide suggestions for similar words if the word is misspelled
        suggestion = get_close_matches(word, data.keys())[0]
        confirmation = input(f"Did you mean '{suggestion}' instead? Enter 'Y' for yes, 'N' for no: ").lower()
        if confirmation == 'y':
            return data[suggestion]
        elif confirmation == 'n':
            return "The word doesn't exist. Please double-check it."
        else:
            return "We didn't understand your input."
    else:
        return "The word doesn't exist. Please double-check it."

def main():
    while True:
        word = input("Enter a word: ")
        if word == "exit":
            break
        definition = get_definition(word)
        if isinstance(definition, list):
            for meaning in definition:
                print(meaning)
        else:
            print(definition)

if __name__ == "__main__":
    main()

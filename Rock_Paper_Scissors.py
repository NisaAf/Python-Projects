import random

def get_user_choice():
    """Get the user's choice (Rock, Paper, or Scissors)."""
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a round of Rock, Paper, Scissors."""
    user_score = 0
    computer_score = 0
    turns = int(input("How many turns do you want to play? "))
    
    for _ in range(turns):
        print("Let's play Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. The computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

    print("Game over!")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

# Main game loop
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

print("Thanks for playing!")

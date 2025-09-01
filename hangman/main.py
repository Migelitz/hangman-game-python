import random
from hangman_words import fruit_words
from hangman_art import hangman_art

# Display the hangman and print out from Hangman_Art
def display_man(wrong_guesses):
    print("________________________")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("________________________")

# Print out the hit like this "_ _ _ _"
def display_hint(hint):
    print(" ".join(hint))

# Shows answer
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(fruit_words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        
        if len(guess) > 1 or not guess.isalpha():
            print("Invalid Input.")
            continue
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Yay! You saved the man!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Man died☠️ (What have you done!?)")
            is_running = False
            
if __name__ == '__main__':
    playing = True
    
    while playing:
        main()
        play_again = input("Play Again? (N to quit): ").upper()
        
        if play_again == "N":
            print("Thanks for playing!")
            print("Exiting the program...")
            playing = False
                
            
    
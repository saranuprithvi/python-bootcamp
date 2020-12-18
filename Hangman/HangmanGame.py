import random
def HangmanFunction():
    turns = 10
    flag = 0
    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" ])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    guess_made = ""
    while len(word)>0:
        main_word = ""
        for letter in word:
            if letter in guess_made:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "
        if main_word == word:
            print(main_word)
            print("You win !")
            break
        print("Guess the word :",main_word)
        guess = input()
        if guess in validLetters:
            guess_made = guess_made + guess
        else:
            print("Enter a valid letter:")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

name = input("Enter your name : ")
print("Welcome " + name + "\n------------------- \nTry to guess the word in less than 10 attempts ")
HangmanFunction()

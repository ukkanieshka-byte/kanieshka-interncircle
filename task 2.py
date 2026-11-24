import random
attempts=0
secret_number=random.randint(1,100)
print("Guess the secret number between 1 to 100")
while True:
    guess=int(input("Enter your guess:"))
    attempts+=1
    if guess<secret_number:
        print("Too low!Try again.")
    elif guess>secret_number:
        print("Too high!Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
text=input("Enter a sentence or paragraph:")
words=text.split()
word_count=len(words)
char_count=len(text.replace(" ",""))
print(f"Total words: {word_count}")
print(f"Total characters (no spaces): {char_count}")

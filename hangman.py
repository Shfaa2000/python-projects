import random

#مراحل هانغ مان بالاسكي
hangman_stages = ["0","1","2","3","4","5"]
random_words = random.choice(["good", "bad", "ugly"])
display = ["_"] * len(random_words)
print(''.join(display))
lives = 6
# قائمة لتخزين الحروف التي تم تخمينها
guessed_letters = []
print(hangman_stages[0])
while "_" in display and lives > 0:
    guessed = input("Please guess a letter: ").lower()

    #هل الحرف تم تخمينه من قبل
    if guessed in guessed_letters:
        print("You already guessed that. Try again.")
        print(f"You have {lives} more tries")
        continue

    #في حالة لم يسبق تخمينها ضيفه للقائمة
    guessed_letters.append(guessed)
    if guessed not in random_words:
        lives -=1
        print(hangman_stages[5-lives])
    else:
        for position in range(len(random_words)):
            if random_words[position] == guessed:
                display[position] = guessed

    print(''.join(display))
    print(f'You have {lives} more tries')
if lives == 0:
    print("You lose")
    print(hangman_stages[-1])
else:
    print("You win")
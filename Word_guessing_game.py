import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)
attemts = 10
guessdword = ['_'] * len(word)

while attemts > 0:
    print('\nCurrent word: ' + ' '.join(guessdword))

    guess = input('Enter your guess: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessdword[i] = guess
        print('Good guess!')

    else:
        attemts -= 1
        print('Wrong! Attempts left: ' + str(attemts))
    if '_' not in guessdword:
        print('\nCongratulations! You guessed the word: ' + word)
        break

if attemts == 0 and '_' in guessdword:
    print('\nYou ran out of attempts. The word was: ' + word)
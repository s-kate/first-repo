import random


fruits_list = ['apple', 'banana', 'pineapple', 'grape', 'peach', 'lemon']
secret_word = random.choice(fruits_list)
number_of_attempts = int(input('Enter number of attempts: '))
guessed_letters = []
final_word = ''

for l1 in secret_word:
    final_word += '*'
    guessed_letters += '*'

while number_of_attempts != 0:
    number_of_attempts -= 1
    user_suppose = input('Enter your suppose: ')

    if len(user_suppose) == 1:
        i = -1

        for letter in secret_word:
            i += 1

            if letter == user_suppose:
                print('yes')
                guessed_letters[i] = letter
                final_word = ''.join(guessed_letters)

            elif secret_word[-1] == letter and letter != user_suppose:
                print('Try again!')
                break

        print(final_word)

    else:
        if user_suppose == secret_word:
            print('Congratulations, you are right!')
            break
        else:
            print('Try again!')
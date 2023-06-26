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
    print(f'attempts: {number_of_attempts}')
    user_suppose = input('Enter your suppose: ')

    if len(user_suppose) == 1:
        i = -1
        is_guessed = False

        for letter in secret_word:
            i += 1

            if letter == user_suppose:
                guessed_letters[i] = letter
                final_word = ''.join(guessed_letters)
                is_guessed = True

            elif i == len(secret_word)-1 and letter != user_suppose and not is_guessed:
                print('Try again!')
                number_of_attempts -= 1
                break

        print(final_word)
        if final_word.find('*') == -1:
            print('Congratulations, you are right!')
            break

    else:
        if user_suppose == secret_word:
            print('Congratulations, you are right!')
            break
        else:
            number_of_attempts -= 1
            print('Try again!')
            
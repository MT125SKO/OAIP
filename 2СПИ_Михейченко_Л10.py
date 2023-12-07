
# Задание 1
import random
all_characters= 'abcdefghijklnopqrstuvwxyz'
a2ll_characters= '1234567890'
a3ll_characters= '!?%№*+=$#@{}[]()^/\|.,'
a4ll_characters= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
long = input('длина пароля?'+ "\n")
long = int(long)
password =''
for i in range(long):
    password += random.choice(all_characters)
    password += random.choice(a2ll_characters)
    password += random.choice(a3ll_characters)
    password += random.choice(a4ll_characters)
    print(password)

# Задание 2. Брутфорс есть, пускай без других знаков.
Password = 4656
for i in range(1, 100000):
	print (i)
	if i == Password:
		print (f'{i}')
		break

# Задание 3 Делал в месте с Никитой
import random
words = ['яблоко']
word = random.choice(words)
hidden_word = [''] * len(word)
attempts = 5
print("Добро пожаловать в игру 'Угадай слово'!")
while '' in hidden_word and attempts > 0:
    print(' '.join(hidden_word))
    guess = input("Угадайте букву: ")
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
        print("Поздравляю, вы угадали букву!")
    else:
        attempts -= 1
        print("Увы, такой буквы в слове нет. У вас осталось {} попыток.".format(attempts))
if '_' not in hidden_word:
    print(' '.join(hidden_word))
    print("Поздравляю, вы угадали слово '{}'!".format(word))
else:
    print("Увы, вы проиграли. Загаданное слово было '{}'.".format(word))

# Задание 4
import random
words = ['Да', 'Нет', 'Скорее всего да', 'Скорее всего нет', 'Возможно','Имеются перспективы', 'Вопрос задан неверно']
word = random.choice(words)
question = input('Введите воспрос: ')
check = question.replace('?', '')
print('Ваш вопрос==>', check, '\nОтвет:', word)
	
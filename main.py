import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

count_pass = int(input("Введите количество паролей: "))
length_pass = int(input('Введите длину пароля: '))
include_digits = True if input("Включать ли цифры в пароль? да / нет: ").lower() == "да" else False
include_lowercase_letters = True if input("Включать ли строчные буквы? да / нет: ").lower() == "да" else False
include_uppercase_letters = True if input("Включать ли прописные буквы? да / нет: ").lower() == "да" else False
include_punctuation = True if input("Включать ли неоднозначные символы? да / нет: ").lower() == "да" else False

if include_digits:
    chars += digits
if include_lowercase_letters:
    chars += lowercase_letters
if include_punctuation:
    chars += punctuation
if include_uppercase_letters:
    chars += uppercase_letters
def generate_password(length, chars):
    if not chars:
        print("Ошибка. Не выбран ни один диапазон символов")
        return
    for i in range(count_pass + 1):
        password = ''
        for j in range(length):
          password += random.choice(chars)
        print(f'Пароль номер {i}: {password}')
generate_password(length_pass, chars)